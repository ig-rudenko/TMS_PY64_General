from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine("sqlite:///users.db", echo=True)  # подключение к БД.

session_maker = sessionmaker(bind=engine, autocommit=False)  # Класс для создания сессий, для работы с БД.


class Base(DeclarativeBase):
    pass
