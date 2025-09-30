from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import UserModel
from src.dto.users import UserDTO
from src.exceptions import ObjectNotFound
from src.repository.abstract import AbstractUserRepository


class SqlAlchemyUsersRepository(AbstractUserRepository):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get(self, user_id: int) -> UserDTO:
        query = select(UserModel).where(UserModel.id == user_id)
        result = await self.session.execute(query)
        user = result.scalar_one_or_none()
        if user is None:
            raise ObjectNotFound(f"User not found")
        return self._to_dto(user)

    async def get_by_username(self, username: str) -> UserDTO:
        pass

    async def create(self, instance: UserDTO) -> UserDTO:
        model = UserModel(
            username=instance.username,
            password=instance.password,
            first_name=instance.first_name,
            last_name=instance.last_name,
            is_active=instance.is_active,
            is_superuser=instance.is_superuser,
            is_staff=instance.is_staff,
        )
        self.session.add(model)
        await self.session.flush()
        await self.session.refresh(model)
        return self._to_dto(model)

    async def update(self, instance: UserDTO) -> UserDTO:
        pass

    @staticmethod
    def _to_dto(model: UserModel) -> UserDTO:
        return UserDTO(
            id=model.id,
            username=model.username,
            password=model.password,
            first_name=model.first_name,
            last_name=model.last_name,
            is_active=model.is_active,
            is_superuser=model.is_superuser,
            is_staff=model.is_staff,
        )
