from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class MessageType(str, Enum):
    text = "text"
    notification = "notification"


class MessageDTO(BaseModel):
    id: int | None = None
    sender_id: int
    recipient_id: int
    message: str = Field(min_length=1, max_length=4096)
    type: MessageType
    created_at: datetime

    # {"sender_id":1,"recipient_id":1,"message":"Hello","type":"text","created_at":"2025-10-07T19:58:47.497831"}


@dataclass(slots=True, kw_only=True)
class MessageFilterDTO:
    between_users: tuple[int, int]
    date_from: datetime
    date_to: datetime = field(default_factory=datetime.now)
    search: str | None = None
