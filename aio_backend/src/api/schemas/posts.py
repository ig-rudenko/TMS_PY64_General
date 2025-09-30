from datetime import datetime

from pydantic import BaseModel, Field


class CreatePostSchema(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    content: str = Field(..., min_length=1)


class ReadPostSchema(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    author: str

    class Config:
        from_attributes = True


class PostsListResponseSchema(BaseModel):
    results: list[ReadPostSchema]
    count: int
