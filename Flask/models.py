from datetime import datetime

from sqlalchemy import String, Integer, Boolean, ForeignKey, func, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

engine = create_engine("sqlite:///database.db", echo=True)
session_maker = sessionmaker(bind=engine, autocommit=False)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(64), unique=True)
    password: Mapped[str] = mapped_column(String(64))
    points: Mapped[int] = mapped_column(Integer, default=0)

    # tickets: Mapped[list["Ticket"]] = relationship("Ticket", back_populates="user")

    @staticmethod
    def is_exist(username: str) -> bool:
        with session_maker() as session:
            if session.query(User).filter(User.username == username).first():
                return True
        return False


class Ticket(Base):
    __tablename__ = "tickets"
    uuid: Mapped[int] = mapped_column(String(36), primary_key=True)
    available: Mapped[bool] = mapped_column(Boolean, default=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="RESTRICT"), nullable=True)

    # user: Mapped["User"] = relationship(User, back_populates="tickets")

    @staticmethod
    def valid_ticket(ticket_uuid: str) -> bool:
        with session_maker() as session:
            if session.query(Ticket).filter(Ticket.uuid == ticket_uuid, Ticket.available == True).first():
                return True
        return False


class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(64))
    cost: Mapped[int] = mapped_column(Integer)
    count: Mapped[int] = mapped_column(Integer)

    # orders: Mapped[list["Order"]] = relationship("Order", back_populates="product")


class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="RESTRICT"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id", ondelete="RESTRICT"))
    count: Mapped[int] = mapped_column(Integer)
    order_datetime: Mapped[datetime] = mapped_column(server_default=func.now())

    # user: Mapped["User"] = relationship(User, back_populates="orders")
    # product: Mapped["Product"] = relationship(Product, back_populates="orders")