from fastapi import APIRouter, Depends, Query, HTTPException

from src.api.depends import get_current_user, get_posts_repo
from src.api.schemas.posts import CreatePostSchema, PostsListResponseSchema, ReadPostSchema
from src.dto.posts import PostCreateDTO
from src.dto.users import UserDTO
from src.repository.abstract import AbstractPostRepository
from src.services.posts import create_post, get_posts_list

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get("", response_model=PostsListResponseSchema)
async def get_posts_api_view(
    page: int = Query(1, gt=0, description="Номер страницы"),
    page_size: int = Query(25, gt=0, le=100, description="Количество постов на странице"),
    search: str = Query("", max_length=255, description="Строка поиска"),
    author: str = Query("", max_length=255, description="Автор поста"),
    repo: AbstractPostRepository = Depends(get_posts_repo),
):
    # http://127.0.0.1:8000/api/v1/posts?page=1&page_size=10
    posts, total_count = await get_posts_list(
        repo, page=page, page_size=page_size, search=search, author_username=author
    )
    posts_schemas = [ReadPostSchema.model_validate(post) for post in posts]
    return PostsListResponseSchema(results=posts_schemas, count=total_count)


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
