from models import Base, engine, User, Product, Order, Ticket
from menu import Menu


def create_tables():
    Base.metadata.create_all(engine)
    print(User)
    print(Product)
    print(Order)
    print(Ticket)


create_tables()
menu = Menu()
menu.run()
