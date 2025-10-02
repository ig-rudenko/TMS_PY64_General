from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine


class DatabaseConnector:

    def __init__(self):
        self._engine: AsyncEngine | None = None
        self._session_maker: async_sessionmaker[AsyncSession] | None = None

    def init(self, url: str):
        self._engine = create_async_engine(
            url=url,
            echo=True,
            pool_pre_ping=True,
        )
        self._session_maker = async_sessionmaker(
            bind=self._engine,
            autocommit=False,
            autoflush=False,
        )

    @asynccontextmanager
    async def session(self):
        if self._session_maker is None:
            raise RuntimeError("DatabaseConnector is not initialized!")

        async with self._session_maker() as session:
            try:
                yield session  # Возвращаем сессию и работаем с ней до выхода из контекста. Ожидаем завершения.
            except Exception as exc:
                print("Error occurred!", exc)
                print("Rolling back...")
                await session.rollback()  # В случае ошибки откатываем все изменения в БД для данной сессии.
                raise
            else:
                print("Committing...")
                await session.commit()  # Сохраняем изменения в БД.


db_connector = DatabaseConnector()
