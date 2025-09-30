from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True, kw_only=True)
class PostDTO:
    id: int
    title: str
    content: str
    created_at: datetime = field(default_factory=datetime.now)
    author: str


@dataclass(slots=True, kw_only=True)
class PostCreateDTO:
    title: str
    content: str
    created_at: datetime = field(default_factory=datetime.now)
    author_id: int
