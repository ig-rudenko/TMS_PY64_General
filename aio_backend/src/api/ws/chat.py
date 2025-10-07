from fastapi import WebSocket, WebSocketDisconnect

from src.api.depends import get_message_repo
from src.database.connector import db_connector
from src.dto.users import UserDTO
from src.api.ws.manager import ws_manager
from src.services.messages import process_new_message


async def process_ws_connection(user: UserDTO, websocket: WebSocket):
    ws_manager.add_connection(user.id, websocket)

    try:
        while True:
            data: str = await websocket.receive_text()  # На паузе, пока не получим данные
            msg = await ws_manager.parse_message(data)
            if msg is None:
                continue

            # Тут можно добавить разрешения на отправку сообщения получателю.
            await ws_manager.send_message(msg.recipient_id, msg)
            async with db_connector.session() as session:  # Это очень не производительно!
                msg_repo = get_message_repo(session)
                await process_new_message(msg, msg_repo)

    except Exception as exc:
        ws_manager.remove_connection(user.id, websocket)
        if not isinstance(exc, WebSocketDisconnect):
            raise exc  # Если это не ошибка закрытия соединения, то пробрасываем дальше.
