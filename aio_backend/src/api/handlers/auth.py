from fastapi import APIRouter, Depends, HTTPException

from src.api.depends import get_token_service, get_users_repo
from src.api.schemas.auth import LoginSchema, RegisterSchema, TokenPairSchema, UserSchema
from src.dto.users import UserDTO, UserLoginDTO
from src.exceptions import UniqueConstraintError
from src.repository.abstract import AbstractUserRepository
from src.services.auth import login_user, register_user
from src.services.token_service import JWTokenService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/token", response_model=TokenPairSchema)
async def get_token_pair_api_view(
    data: LoginSchema,
    repo: AbstractUserRepository = Depends(get_users_repo),
    token_service: JWTokenService = Depends(get_token_service),
):
    return await login_user(repo, token_service, UserLoginDTO(username=data.username, password=data.password))


@router.post("/register", response_model=UserSchema, status_code=201)
async def register_user_api_view(
    data: RegisterSchema,
    repo: AbstractUserRepository = Depends(get_users_repo),
):
    try:
        return await register_user(
            repo,
            UserDTO(
                id=0,
                username=data.username,
                password=data.password,
                first_name=data.first_name,
                last_name=data.last_name,
            ),
        )
    except UniqueConstraintError as exc:
        raise HTTPException(status_code=422, detail="Пользователь с таким username уже существует") from exc
