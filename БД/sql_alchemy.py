from sqlalchemy import String, create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, sessionmaker


class Base(DeclarativeBase):
    pass


class User(Base):  # Модель пользователя
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(128), unique=True)
    email: Mapped[str] = mapped_column(String(254), unique=True)
    password: Mapped[str] = mapped_column(String(128))  # По умолчанию не NULL

    def __repr__(self) -> str:
        return f"User(id={self.id}, username={self.username}, email={self.email}, password={self.password})"


engine = create_engine("sqlite:///users.db", echo=True)  # подключение к БД.

Base.metadata.create_all(engine)  # Создание таблиц.

session_maker = sessionmaker(bind=engine, autocommit=False)  # Класс для создания сессий, для работы с БД.


def add_user(username: str, email: str, password: str) -> None:
    session = session_maker()  # Создание сессии
    user = User(username=username, email=email, password=password)
    session.add(user)  # Добавление пользователя в сессию
    session.commit()  # Сохранение изменений
    session.close()  # Закрытие сессии


def show_users() -> None:
    session = session_maker()
    for user in session.query(User).all():
        print(user)


try:
    add_user("test", "test@test.ru", "test")
    add_user("test2", "test2@test.ru", "test2")
except IntegrityError:
    print("Пользователь уже существует")
show_users()
