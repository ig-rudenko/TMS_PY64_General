import pickle
from typing import Any

from redis.asyncio import ConnectionPool, Redis

from src.services.cache.base import AbstractCache


class RedisCache(AbstractCache):

    def __init__(self, url: str, max_connections: int = 5):
        self._pool = ConnectionPool.from_url(
            url=url,
            max_connections=max_connections,
        )
        self._redis = Redis(connection_pool=self._pool)

    async def get(self, key: str) -> Any | None:
        value = await self._redis.get(key)
        if value is not None:
            return pickle.loads(value)
        return None

    async def put(self, key: str, value: Any, ttl: int) -> bool:
        await self._redis.set(key, pickle.dumps(value), ex=ttl)
        return True

    async def delete(self, key: str) -> bool:
        await self._redis.delete(key)
        return True
