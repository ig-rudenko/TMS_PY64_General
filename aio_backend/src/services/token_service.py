from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from typing import Literal

import jwt
from pydantic import BaseModel, ValidationError

from src.exceptions import InvalidTokenError


@dataclass(frozen=True, kw_only=True, slots=True)
class JWTokenPair:
    access: str
    refresh: str


class Payload(BaseModel):
    sub: str  # user id
    type: Literal["access", "refresh"]
    iat: int  # Время создания
    exp: int  # Время истечения


class JWTokenService:

    def __init__(self, secret: str, access_exp_min: int, refresh_exp_days: int):
        self._secret = secret
        self._access_exp_min = access_exp_min
        self._refresh_exp_days = refresh_exp_days

    def create_token_pair(self, user_id: int) -> JWTokenPair:
        access = self._create_token(user_id, "access")
        refresh = self._create_token(user_id, "refresh")
        return JWTokenPair(
            access=access,
            refresh=refresh,
        )

    def get_user_id(self, token: str) -> int:
        payload = self._validate_token(token, "access")
        return int(payload.sub)

    def refresh_token_pair(self, token: str) -> JWTokenPair:
        payload = self._validate_token(token, "refresh")
        return self.create_token_pair(int(payload.sub))

    def _validate_token(self, token: str, type_: Literal["access", "refresh"]) -> Payload:
        try:
            payload = Payload.model_validate(jwt.decode(token, self._secret, algorithms=["HS256"]))
        except jwt.exceptions.InvalidTokenError as exc:
            raise InvalidTokenError("Invalid token") from exc
        except ValidationError as exc:
            raise InvalidTokenError("Invalid token payload") from exc
        if payload.type != type_:
            raise InvalidTokenError(f"Token type is not {type_}")
        if payload.exp < datetime.now(UTC).timestamp():
            raise InvalidTokenError("Token is expired")
        if not payload.sub.isdigit():
            raise InvalidTokenError("User id is not digit string")
        return payload

    def _create_token(self, user_id: int, type_: Literal["access", "refresh"]) -> str:
        now = datetime.now(UTC)
        exp = now
        if type_ == "access":
            exp += timedelta(minutes=self._access_exp_min)
        elif type_ == "refresh":
            exp += timedelta(days=self._refresh_exp_days)

        payload = Payload(
            sub=str(user_id),
            iat=int(now.timestamp()),
            exp=int(exp.timestamp()),
            type=type_,
        )

        token = jwt.encode(payload.model_dump(mode="json"), self._secret, algorithm="HS256")
        return token
