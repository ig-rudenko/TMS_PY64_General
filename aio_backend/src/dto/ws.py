from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class MessageType(str, Enum):
    text = "text"
    notification = "notification"


class WSMessageDTO(BaseModel):
    sender_id: int
    recipient_id: int
    message: str
    type: MessageType
    created_at: datetime
