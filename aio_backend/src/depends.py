from src.repository.abstract import AbstractPostRepository, AbstractUserRepository
from src.repository.posts_repo import FakePostsRepository
from src.repository.users_repo import FakeUsersRepository
from src.services.token_service import JWTokenService
from src.settings import settings


def get_posts_repo() -> AbstractPostRepository:
    return FakePostsRepository()


def get_users_repo() -> AbstractUserRepository:
    return FakeUsersRepository()


def get_token_service() -> JWTokenService:
    return JWTokenService(
        secret=settings.jwt_secret,
        access_exp_min=settings.access_exp_min,
        refresh_exp_days=settings.refresh_exp_days,
    )
