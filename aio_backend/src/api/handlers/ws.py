from fastapi import APIRouter, Depends, WebSocket

from src.api.depends import get_user_and_websocket
from src.api.ws.chat import process_ws_connection
from src.dto.users import UserDTO

router = APIRouter(prefix="/ws", tags=["websocket"])


@router.websocket("")
async def websocket_endpoint(
    ws_pair: tuple[UserDTO, WebSocket] | None = Depends(get_user_and_websocket),
):
    if ws_pair is None:
        return
    user, websocket = ws_pair

    await websocket.accept()
    await process_ws_connection(user=user, websocket=websocket)
