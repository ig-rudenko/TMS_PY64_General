from src.dto.posts import PostDTO
from src.repository.posts_repo import FakePostsRepository


async def get_posts_list() -> list[PostDTO]:
    repo = FakePostsRepository()
    resp = await repo.get_posts()
    # Тут можно добавить кеш.
    return resp


async def create_post(title: str, content: str, owner_id: int) -> PostDTO:
    repo = FakePostsRepository()
    return await repo.create_post(title=title, content=content, owner_id=owner_id)
