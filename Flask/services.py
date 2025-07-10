from sqlalchemy import select

from models import session_maker, User, Product, Order


class BuyProductException(Exception):
    pass


def create_product(name: str, cost: int, count: int) -> Product:
    with session_maker() as session:
        product = Product(name=name, cost=cost, count=count)
        session.add(product)
        session.commit()
        session.refresh(product)
        return product


def create_user(username: str, password: str) -> User:
    with session_maker() as session:
        user = User(username=username, password=password)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user


def get_user(username: str, password: str) -> User | None:
    with session_maker() as session:
        user = session.query(User).filter(User.username == username, User.password == password).first()
        return user


def get_all_products() -> list[Product]:
    with session_maker() as session:
        query = select(Product).order_by(Product.id.desc())
        products = session.execute(query).scalars().all()
        return list(products)


def buy_product(user_id: int, product_id: int, count: int) -> Order:
    with session_maker() as session:
        user = session.get(User, user_id)
        if user is None:
            raise BuyProductException("Пользователь с таким ID не найден!")

        product = session.get(Product, product_id)
        if product is None:
            raise BuyProductException("Продукт с таким ID не найден!")

        if product.count < count:
            raise BuyProductException("Недостаточно товара на складе!")

        total_price = product.cost * count

        if user.points < total_price:
            raise BuyProductException("Недостаточно поинтов для покупки!")

        user.points -= total_price
        product.count -= count
        order = Order(user_id=user_id, product_id=product_id, count=count)

        session.add(order)
        session.commit()
        session.refresh(order)

        return order
