from src.dto.users import UserDTO
from .base import AbstractCache


class UserCacheService:
    cache_prefix = "user_info"

    def __init__(self, cache: AbstractCache, cache_ttl: int = 60):
        self.cache = cache
        self.ttl = cache_ttl

    def get_cache_key(self, user_id: int | str) -> str:
        return f"{self.cache_prefix}:{user_id}"

    async def get_user(self, user_id: int | str) -> UserDTO | None:
        cache_key = self.get_cache_key(user_id)
        return await self.cache.get(cache_key)

    async def set_user(self, user_id: int | str, user: UserDTO) -> None:
        cache_key = self.get_cache_key(user_id)
        await self.cache.put(cache_key, value=user, ttl=self.ttl)

    async def delete_user(self, user_id: int | str) -> None:
        cache_key = self.get_cache_key(user_id)
        await self.cache.delete(cache_key)


class UserOnlineStatusService:
    cache_prefix = "user_online_status"

    def __init__(self, cache: AbstractCache, cache_ttl: int = 30):
        self.cache = cache
        self.ttl = cache_ttl

    def get_cache_key(self, user_id: int | str) -> str:
        return f"{self.cache_prefix}:{user_id}"

    async def set_online(self, user_id: int):
        cache_key = self.get_cache_key(user_id)
        await self.cache.put(cache_key, value=True, ttl=self.ttl)

    async def set_offline(self, user_id: int):
        cache_key = self.get_cache_key(user_id)
        await self.cache.put(cache_key, value=False, ttl=self.ttl)

    async def is_online(self, user_id: int) -> bool:
        cache_key = self.get_cache_key(user_id)
        return bool(await self.cache.get(cache_key))
