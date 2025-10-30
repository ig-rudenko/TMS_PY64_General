from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import MessageModel
from src.dto.messages import MessageDTO, MessageFilterDTO
from src.exceptions import ObjectNotFound
from src.repository.abstract import AbstractMessageRepository


class SqlAlchemyMessageRepository(AbstractMessageRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, msg_id: int) -> MessageDTO:
        query = select(MessageModel).where(MessageModel.id == msg_id)
        result = await self.session.execute(query)
        post = result.scalar_one_or_none()
        if post is None:
            raise ObjectNotFound(f"Message with id {msg_id} not found")
        return self._to_dto(post)

    async def filter_messages(self, filter_: MessageFilterDTO) -> list[MessageDTO]:
        return []

    async def create(self, instance: MessageDTO) -> MessageDTO:
        msg = self._to_model(instance)
        self.session.add(msg)  # Добавляем объект в сессию.
        await self.session.flush()  # Передаём изменения в БД для текущей сессии.
        await self.session.refresh(msg)  # Обновляем объект, чтобы получить id.
        return self._to_dto(msg)

    async def update(self, instance: MessageDTO) -> MessageDTO:  # type: ignore
        pass

    async def delete(self, msg_id: int) -> None:  # type: ignore
        pass

    @staticmethod
    def _to_dto(model: MessageModel) -> MessageDTO:
        return MessageDTO(
            id=model.id,
            sender_id=model.sender_id,
            recipient_id=model.recipient_id,
            message=model.message,
            type=model.type,
            created_at=model.created_at,
        )

    @staticmethod
    def _to_model(dto: MessageDTO) -> MessageModel:
        return MessageModel(
            id=dto.id,
            sender_id=dto.sender_id,
            recipient_id=dto.recipient_id,
            message=dto.message,
            type=dto.type,
            created_at=dto.created_at,
        )
