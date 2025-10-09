from passlib.context import CryptContext

from .cache.base import AbstractCache
from .cache.services import UserCacheService
from ..dto.users import UserDTO, UserLoginDTO
from ..exceptions import AuthenticationError
from ..repository.abstract import AbstractUserRepository
from .token_service import JWTokenPair, JWTokenService

__context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return __context.hash(password)


def verify_password(password: str, *, hashed_password: str) -> bool:
    return __context.verify(password, hashed_password)


async def login_user(
    repo: AbstractUserRepository, token_service: JWTokenService, data: UserLoginDTO
) -> JWTokenPair:
    user = await repo.get_by_username(data.username)
    if not verify_password(data.password, hashed_password=user.password):
        raise AuthenticationError("Invalid username or password")

    return token_service.create_token_pair(user.id)


async def register_user(repo: AbstractUserRepository, data: UserDTO, cache: AbstractCache) -> UserDTO:
    data.password = get_password_hash(data.password)
    user = await repo.create(data)
    user_cache_service = UserCacheService(cache)
    await user_cache_service.set_user(user.id, user)
    return user


async def update_user(repo: AbstractUserRepository, user_data: UserDTO, cache: AbstractCache) -> UserDTO:
    user = await repo.update(user_data)

    user_cache_service = UserCacheService(cache)
    await user_cache_service.delete_user(user.id)
    return user
