from fastapi import APIRouter, Depends

from src.api.depends import get_posts_repo, get_current_user, get_user_or_none
from src.database.connector import db_connector
from src.dto.posts import PostCreateDTO
from src.dto.users import UserDTO
from src.repository.abstract import AbstractPostRepository
from src.api.schemas.posts import PostsListResponseSchema, ReadPostSchema, CreatePostSchema
from src.services.posts import get_posts_list, create_post

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get("", response_model=PostsListResponseSchema)
async def get_posts_api_view(
    repo: AbstractPostRepository = Depends(get_posts_repo),
):
    posts = await get_posts_list(repo)
    posts_schemas = [ReadPostSchema.model_validate(post) for post in posts]
    return PostsListResponseSchema(
        results=posts_schemas,
        count=len(posts),
    )


@router.post("", response_model=ReadPostSchema)
async def create_post_api_view(
    data: CreatePostSchema,
    repo: AbstractPostRepository = Depends(get_posts_repo),
    user: UserDTO = Depends(get_current_user),
):
    return await create_post(
        repo=repo,
        new_post=PostCreateDTO(
            title=data.title,
            content=data.content,
            author_id=user.id,
        ),
    )
