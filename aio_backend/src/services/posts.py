from src.dto.posts import PostDTO, PostCreateDTO
from src.repository.abstract import AbstractPostRepository


async def get_posts_list(repo: AbstractPostRepository) -> list[PostDTO]:
    resp = await repo.get_list()
    # Тут можно добавить кеш.
    return resp


async def create_post(repo: AbstractPostRepository, new_post: PostCreateDTO) -> PostDTO:
    return await repo.create(new_post)
