import re
from collections.abc import AsyncIterator
from functools import cache

from fastapi import Depends, Header, HTTPException, WebSocket
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.connector import db_connector
from src.database.repo.message_repo import SqlAlchemyMessageRepository
from src.database.repo.posts_repo import SqlAlchemyPostRepository
from src.database.repo.users_repo import SqlAlchemyUsersRepository
from src.dto.users import UserDTO
from src.exceptions import InvalidTokenError, ObjectNotFound
from src.repository.abstract import AbstractMessageRepository, AbstractPostRepository, AbstractUserRepository
from src.services.cache.base import AbstractCache
from src.services.cache.redis import RedisCache
from src.services.cache.services import UserCacheService
from src.services.token_service import JWTokenService
from src.settings import CacheType, settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")


def get_token_service() -> JWTokenService:
    return JWTokenService(
        secret=settings.jwt_secret,
        access_exp_min=settings.access_exp_min,
        refresh_exp_days=settings.refresh_exp_days,
    )


async def get_session() -> AsyncIterator[AsyncSession]:
    async with db_connector.session() as session:  # Открываем сессию для работы с БД.
        yield session


def get_users_repo(session: AsyncSession = Depends(get_session)) -> AbstractUserRepository:
    return SqlAlchemyUsersRepository(session)


def get_posts_repo(session: AsyncSession = Depends(get_session)) -> AbstractPostRepository:
    return SqlAlchemyPostRepository(session)


def get_message_repo(session: AsyncSession = Depends(get_session)) -> AbstractMessageRepository:
    return SqlAlchemyMessageRepository(session)


@cache
def get_cache() -> AbstractCache:
    if settings.cache_type == CacheType.REDIS:
        return RedisCache(url=settings.cache_url, max_connections=settings.cache_max_connections)
    raise ValueError("Set Cache to Redis")


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    user_repo: AbstractUserRepository = Depends(get_users_repo, use_cache=True),
    token_service: JWTokenService = Depends(get_token_service),
    cache: AbstractCache = Depends(get_cache),
) -> UserDTO:
    try:
        user_id = token_service.get_user_id(token)
    except InvalidTokenError as exc:
        raise HTTPException(detail=str(exc), status_code=401) from exc

    user_cache_service = UserCacheService(cache, cache_ttl=settings.access_exp_min * 60)
    user = await user_cache_service.get_user(user_id)
    if user is not None:
        return user

    try:
        user = await user_repo.get(user_id)
    except ObjectNotFound as exc:
        raise HTTPException(detail="User not found", status_code=401) from exc

    await user_cache_service.set_user(user_id, user)  # Добавляем в кэш пользователя.

    if not user.is_active:
        raise HTTPException(
            detail=f"User {user.username} is not active ghsjdkfhgjkhsjkdfh klsghldf kjhkglsj dhlkfjgh klsjdhf klgjhsdklfjh glksjhdfkljg hksldhfjklg hsjkldhf klhskldf hklh ",
            status_code=401,
        )

    return user


async def get_user_or_none(
    authorization: str | None = Header(None),
    user_repo: AbstractUserRepository = Depends(get_users_repo, use_cache=True),
    token_service: JWTokenService = Depends(get_token_service),
) -> UserDTO | None:
    if authorization is None:
        return None

    token_match = re.match(r"^(Bearer) (?P<token>\S+)$", authorization)
    if token_match is None:
        return None

    return await get_current_user(token_match.group("token"), user_repo, token_service)


async def get_user_and_websocket(
    websocket: WebSocket,
    user_repo: AbstractUserRepository = Depends(get_users_repo, use_cache=True),
    token_service: JWTokenService = Depends(get_token_service),
) -> tuple[UserDTO, WebSocket] | None:

    authorization = websocket.headers.get("authorization")
    if authorization is None:
        await websocket.close(code=1008, reason="Missing token")
        return None

    token_match = re.match(r"^(Bearer) (?P<token>\S+)$", authorization)
    if token_match is None:
        await websocket.close(code=1008, reason="Missing token")
        return None

    try:
        user_id = token_service.get_user_id(token_match.group("token"))
    except InvalidTokenError:
        await websocket.close(code=1008, reason="Invalid token")
        return None

    try:
        user = await user_repo.get(user_id)
    except ObjectNotFound:
        await websocket.close(code=1008, reason="User not found")
        return None

    if not user.is_active:
        await websocket.close(code=1008, reason=f"User {user.username} is not active")
        return None

    return user, websocket
