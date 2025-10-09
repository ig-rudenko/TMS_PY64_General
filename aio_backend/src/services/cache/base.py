from abc import ABC, abstractmethod
from typing import Any


class AbstractCache(ABC):

    @abstractmethod
    async def get(self, key: str) -> Any | None: ...

    @abstractmethod
    async def put(self, key: str, value: Any, ttl: int) -> bool:
        """
        Args:
            key: Строка ключа.
            value: Любое `pickle` сериализуемое значение.
            ttl: Время жизни в секундах.
        """

    @abstractmethod
    async def delete(self, key: str) -> bool: ...
