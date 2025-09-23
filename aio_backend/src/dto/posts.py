from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True, kw_only=True)
class PostDTO:
    id: int
    title: str
    content: str
    created_at: datetime = field(default_factory=datetime.now)
    author: str

    def get_short_content(self):
        if len(self.content) > 100:
            return self.content[:100] + "..."
        else:
            return self.content
