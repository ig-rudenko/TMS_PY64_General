from src.dto.messages import MessageDTO
from src.repository.abstract import AbstractMessageRepository


async def process_new_message(msg: MessageDTO, msg_repo: AbstractMessageRepository) -> None:
    await msg_repo.create(msg)  # Сохраняем сообщение в БД.
    # Можно ещё:
    # Добавлять в очередь сообщение, чтобы другие сервисы его обработали.
    # Изменять кэш кол-ва непрочитанных сообщений пользователя.
    # Изменять кэш последнего сообщения пользователя.
