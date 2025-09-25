from pydantic import BaseModel, Field


class LoginSchema(BaseModel):
    username: str = Field(..., max_length=150)
    password: str = Field(..., max_length=150)


class TokenPairSchema(BaseModel):
    access: str
    refresh: str
