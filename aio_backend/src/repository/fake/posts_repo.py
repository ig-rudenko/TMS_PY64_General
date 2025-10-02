from faker import Faker

from src.dto.posts import PostCreateDTO, PostDTO
from src.repository.abstract import AbstractPostRepository


class FakePostsRepository(AbstractPostRepository):

    def __init__(self, language="en_US"):
        self.fake = Faker(language=language)

    async def get(self, post_id: int) -> PostDTO:
        return PostDTO(
            id=post_id,
            title=self.fake.sentence(),
            content=self.fake.paragraph(50),
            created_at=self.fake.date_time(),
            author=self.fake.name(),
        )

    async def create(self, instance: PostCreateDTO) -> PostDTO:
        return PostDTO(
            id=self.fake.random_int(),
            title=instance.title,
            content=instance.content,
            created_at=self.fake.date_time(),
            author=self.fake.name(),
        )

    async def get_list(self, page: int, page_size: int, search: str = "") -> list[PostDTO]:
        return [
            PostDTO(
                id=i,
                title=self.fake.sentence(),
                content=self.fake.paragraph(50),
                created_at=self.fake.date_time(),
                author=self.fake.name(),
            )
            for i in range(20)
        ]

    async def update(self, instance: PostDTO) -> PostDTO:
        return instance

    async def delete(self, post_id: int) -> None:
        pass
