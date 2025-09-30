from dataclasses import dataclass


@dataclass(slots=True, kw_only=True)
class UserDTO:
    id: int
    username: str
    password: str
    first_name: str
    last_name: str
    is_active: bool = True
    is_superuser: bool = False
    is_staff: bool = False


@dataclass(slots=True, kw_only=True, frozen=True)
class UserLoginDTO:
    username: str
    password: str
