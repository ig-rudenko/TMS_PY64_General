from dataclasses import dataclass


@dataclass(slots=True, kw_only=True)
class UserDTO:
    id: int
    username: str
    password: str
    first_name: str
    last_name: str


@dataclass(slots=True, kw_only=True, frozen=True)
class UserLoginDTO:
    username: str
    password: str
