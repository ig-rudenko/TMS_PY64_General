from pydantic import BaseModel, Field


class LoginSchema(BaseModel):
    username: str = Field(..., max_length=150)
    password: str = Field(..., max_length=150)


class RegisterSchema(LoginSchema):
    first_name: str = Field("", max_length=150)
    last_name: str = Field("", max_length=150)


class UserSchema(BaseModel):
    username: str = Field(..., max_length=150)
    first_name: str = Field(..., max_length=150)
    last_name: str = Field(..., max_length=150)
    is_active: bool
    is_staff: bool
    is_superuser: bool


class TokenPairSchema(BaseModel):
    access: str
    refresh: str
