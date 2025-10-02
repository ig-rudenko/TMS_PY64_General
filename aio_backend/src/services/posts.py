from src.dto.posts import PostCreateDTO, PostDTO
from src.repository.abstract import AbstractPostRepository


async def get_posts_list(
    repo: AbstractPostRepository, page: int, page_size: int, search: str = "", author_username: str = ""
) -> tuple[list[PostDTO], int]:
    resp = await repo.get_list(page=page, page_size=page_size, search=search, author_username=author_username)
    # Тут можно добавить кеш.
    return resp


async def create_post(repo: AbstractPostRepository, new_post: PostCreateDTO) -> PostDTO:
    return await repo.create(new_post)
