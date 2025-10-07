from fastapi import WebSocket
from pydantic import ValidationError

from src.dto.messages import MessageDTO


class WSConnectionManager:

    def __init__(self):
        # За идентификатором пользователя закрепляются все его соединения.
        self._connections: dict[int, list[WebSocket]] = {}

    def add_connection(self, user_id: int, websocket: WebSocket):
        if user_id not in self._connections:
            # Если пользователя нет в списке, то добавляем его.
            self._connections[user_id] = []

        self._connections[user_id].append(websocket)

        # Либо можно просто:
        # self._connections.setdefault(user_id, []).append(websocket)

    def remove_connection(self, user_id: int, websocket: WebSocket):
        if user_id in self._connections:
            # Если соединение есть, то удаляем его.
            try:
                self._connections[user_id].remove(websocket)
            except (ValueError, KeyError):
                pass

    @staticmethod
    async def parse_message(data: str) -> MessageDTO | None:
        try:
            msg = MessageDTO.model_validate_json(data)
            return msg
        except ValidationError as exc:
            print(exc)

    async def send_message(self, user_id: int, message: MessageDTO):
        for ws in self._connections.get(user_id, []):
            if ws:
                await ws.send_text(message.model_dump_json())
            else:
                # Если соединение закрыто, то удаляем его из списка.
                self.remove_connection(user_id, ws)


ws_manager = WSConnectionManager()
