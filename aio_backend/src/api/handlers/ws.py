from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from src.services.ws.manager import ws_manager

router = APIRouter(prefix="/ws", tags=["websocket"])


@router.websocket("")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    ws_manager.add_connection(1, websocket)

    try:
        while True:
            data: str = await websocket.receive_text()  # На паузе, пока не получим данные
            msg = await ws_manager.parse_message(data)
            if msg is None:
                continue
            await ws_manager.send_message(1, msg)
    except WebSocketDisconnect:
        ws_manager.remove_connection(1, websocket)
