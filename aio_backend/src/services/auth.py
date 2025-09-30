from passlib.context import CryptContext

from .token_service import JWTokenService, JWTokenPair
from ..dto.users import UserLoginDTO, UserDTO
from ..exceptions import AuthenticationError
from ..repository.abstract import AbstractUserRepository

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


async def register_user(repo: AbstractUserRepository, data: UserDTO) -> UserDTO:
    data.password = get_password_hash(data.password)
    return await repo.create(data)
