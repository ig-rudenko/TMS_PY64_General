from fastapi import APIRouter

from src.schemas.posts import PostsListResponseSchema, ReadPostSchema, CreatePostSchema
from src.services.posts import get_posts_list, create_post

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get("", response_model=PostsListResponseSchema)
async def get_posts_api_view():
    posts = await get_posts_list()
    posts_schemas = [
        ReadPostSchema.model_validate(post)
        for post in posts
    ]
    return PostsListResponseSchema(
        results=posts_schemas,
        count=len(posts),
    )


@router.post("", response_model=ReadPostSchema)
async def create_post_api_view(data: CreatePostSchema):
    return await create_post(title=data.title, content=data.content, owner_id=123)
