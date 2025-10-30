import re
from typing import Never

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase

from src.exceptions import RepositoryError, UniqueConstraintError


class BaseModel(DeclarativeBase):
    pass


def exception_handler(exc: Exception) -> Never:
    if isinstance(exc, IntegrityError) and "UNIQUE constraint failed" in str(exc):
        filed_match = re.search(r"UNIQUE constraint failed: users\.(\S+)", str(exc))
        if filed_match is not None:
            raise UniqueConstraintError(
                f"Unique constraint failed in field: `{filed_match.group(1)}`"
            ) from exc

    raise RepositoryError("Repository error") from exc
