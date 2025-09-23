from enum import Enum

from pydantic_settings import BaseSettings


class CacheType(str, Enum):
    """
    Возможные типы кэша.
    """
    REDIS = "redis"
    MEMORY = "memory"


class Settings(BaseSettings):
    database_url: str

    cache_type: CacheType = CacheType.MEMORY  # 'redis' or 'memory'

    class Config:
        env_file = ".env"


settings = Settings()  # type: ignore
