from datetime import datetime

from sqlalchemy import String, Text, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


class User(Base):  # Модель пользователя
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(128), unique=True)
    email: Mapped[str] = mapped_column(String(254), unique=True)
    password: Mapped[str] = mapped_column(String(128))  # По умолчанию не NULL

    # Связь с таблицей "notes". Не создается в БД!!!!!
    notes: Mapped[list["Note"]] = relationship("Note", lazy="select", back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id}, username={self.username}, email={self.email}, password={self.password})"


class Note(Base):  # Модель заметки
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(256))
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="RESTRICT"))

    # Связь с таблицей "users". Не создается в БД!!!!!
    user: Mapped["User"] = relationship("User", lazy="select", back_populates="notes")

    def __repr__(self) -> str:
        return (
            f"Notes(id={self.id}, title={self.title}, created_at={self.created_at}, user_id={self.user_id})"
        )
