from faker import Faker

from src.dto.posts import PostDTO


class FakePostsRepository:

    def __init__(self, language="en_US"):
        self.fake = Faker(language=language)

    async def get_posts(self) -> list[PostDTO]:
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

    async def get_post(self, post_id) -> PostDTO:
        return PostDTO(
            id=post_id,
            title=self.fake.sentence(),
            content=self.fake.paragraph(50),
            created_at=self.fake.date_time(),
            author=self.fake.name(),
        )

    async def create_post(self, title, content, owner_id) -> PostDTO:
        return PostDTO(
            id=self.fake.random_int(),
            title=title,
            content=content,
            created_at=self.fake.date_time(),
            author=self.fake.name(),
        )
