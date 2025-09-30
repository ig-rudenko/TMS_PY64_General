import re
from typing import AsyncIterator

from fastapi import Depends, HTTPException, Header
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.connector import db_connector
from src.database.repo.posts_repo import SqlAlchemyPostRepository
from src.database.repo.users_repo import SqlAlchemyUsersRepository
from src.dto.users import UserDTO
from src.exceptions import InvalidTokenError, ObjectNotFound
from src.repository.abstract import AbstractPostRepository, AbstractUserRepository
from src.repository.fake.users_repo import FakeUsersRepository
from src.services.token_service import JWTokenService
from src.settings import settings


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


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    user_repo: AbstractUserRepository = Depends(get_users_repo, use_cache=True),
    token_service: JWTokenService = Depends(get_token_service),
) -> UserDTO:
    try:
        user_id = token_service.get_user_id(token)
    except InvalidTokenError as exc:
        raise HTTPException(detail=str(exc), status_code=401) from exc
    try:
        user = await user_repo.get(user_id)
    except ObjectNotFound as exc:
        raise HTTPException(detail=f"User not found", status_code=401) from exc
    if not user.is_active:
        raise HTTPException(detail=f"User {user.username} is not active", status_code=401)
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
