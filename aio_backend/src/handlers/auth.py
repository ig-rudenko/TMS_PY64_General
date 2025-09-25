from fastapi import APIRouter, Depends

from src.depends import get_users_repo, get_token_service
from src.dto.users import UserLoginDTO
from src.repository.abstract import AbstractUserRepository
from src.schemas.auth import TokenPairSchema, LoginSchema
from src.services.auth import login_user

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/token", response_model=TokenPairSchema)
async def get_token_pair(
    data: LoginSchema,
    repo: AbstractUserRepository = Depends(get_users_repo),
    token_service=Depends(get_token_service),
):
    return await login_user(repo, token_service, UserLoginDTO(username=data.username, password=data.password))
