from faker import Faker

from src.repository.abstract import AbstractUserRepository
from src.dto.users import UserDTO


class FakeUsersRepository(AbstractUserRepository):
    def __init__(self, language="en_US"):
        self.fake = Faker(language=language)

    async def get(self, user_id: int) -> UserDTO:
        return UserDTO(
            id=user_id,
            username=self.fake.user_name(),
            password=self.fake.password(),
            first_name=self.fake.first_name(),
            last_name=self.fake.last_name(),
        )

    async def get_by_username(self, username: str) -> UserDTO:
        return UserDTO(
            id=1,
            username=username,
            password="$2b$12$vBXVUVQKWA2wpgOOIj.U2u3CZvWr7SSVT2BV0GfYSg2uqehiI8tbK",
            first_name=self.fake.first_name(),
            last_name=self.fake.last_name(),
        )

    async def create(self, instance: UserDTO) -> UserDTO:
        pass

    async def update(self, instance: UserDTO) -> UserDTO:
        pass
