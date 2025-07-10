from models import User
from services import create_user, get_user, get_all_products, buy_product, BuyProductException

welcome_text = """
================================================
    === Добро пожаловать в "Не магазин" ===
"""

menu_non_registered = """
    Доступные действия:
    > Товары
    > Зарегистрироваться
    > Войти
    > Выйти
"""

menu_registered = """
    Доступные действия:
    > Товары
    > Купить
    > Профиль
    > Тикет
    > Выйти
"""


class ExitException(Exception):
    pass



class Menu:

    def __init__(self):
        self._user: User | None = None

    def get_commands_text(self) -> str:
        text = """\nДля взаимодействия используйте команды:\n"""
        if self._user is None:
            text += menu_non_registered
        else:
            text += menu_registered

        return text

    def welcome(self) -> str:
        return welcome_text + self.get_commands_text()

    def process_action(self, action: str) -> str:
        action = action.lower().strip()

        if action == "товары":
            return process_show_products_action(action)

        elif action.startswith("купить"):
            if self._user is None:
                return "Для покупки товара необходимо войти в аккаунт"
            return process_buy_product_action(action, self._user.id)

        elif action.startswith("тикет"):
            if self._user is None:
                return "Для добавления тикета необходимо войти в аккаунт"

        elif action == "зарегистрироваться":
            if self._user is not None:
                return "Вы уже зарегистрированы"
            self._user = process_registered_action(action)
            return "Регистрация прошла успешно" if self._user is not None else "Регистрация не удалась"

        elif action == "войти":
            if self._user is not None:
                return "Вы уже вошли"
            self._user = process_login_action(action)
            return "Вход выполнен" if self._user is not None else "Вход не выполнен"

        elif action == "профиль":
            if self._user is None:
                return "Для просмотра профиля необходимо войти в аккаунт"

        elif action == "выйти":
            raise ExitException()

    def run(self):
        print(self.welcome())

        while True:

            try:
                action = input("Введите команду: ")
                print(self.process_action(action))

            except ExitException:
                print("До свидания!")
                break

            print(self.get_commands_text())


def process_registered_action(action: str) -> User | None:
    username = input("Введите имя пользователя: ")
    if User.is_exist(username):
        print("Пользователь с таким именем уже существует")
        return None

    while True:
        password1 = input("Введите пароль: ")
        password2 = input("Повторите пароль: ")
        if password1 == password2:
            break
        print("Пароли не совпадают")

    return create_user(username, password1)


def process_login_action(action: str) -> User | None:
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    user = get_user(username, password)
    if user is None:
        print("Неверный логин или пароль")
    return user


def process_show_products_action(action: str) -> str:
    products = get_all_products()
    max_id_col_width = max(len("ID"), len(str(max(product.id for product in products))))
    max_cost_col_width = max(len("Стоимость"), len(str(max(product.cost for product in products))))
    max_count_col_width = max(len("Кол-во"), len(str(max(product.count for product in products))))
    max_name_col_width = max(len("Название"), len(str(max(product.name for product in products))))

    text = f" {'ID':<{max_id_col_width}} | {'Стоимость':<{max_cost_col_width}} | {'Кол-во':<{max_count_col_width}} | {'Название':<{max_name_col_width}}\n"
    text += "=" * len(text) + "\n"

    for product in products:
        text += f" {product.id:<{max_id_col_width}} | {product.cost:<{max_cost_col_width}} | {product.count:<{max_count_col_width}} | {product.name:<{max_name_col_width}}\n"

    return text


def process_buy_product_action(action: str, user_id: int) -> str:
    action_parts = action.split()
    if len(action_parts) != 3:
        return "Неверный формат команды, введите 'купить <id> <количество>'"
    if not action_parts[1].isdigit() or not action_parts[2].isdigit():
        return "Неверный формат команды, `<id> и <количество>` должны быть числами"
    try:
        order = buy_product(user_id, int(action_parts[1]), int(action_parts[2]))
    except BuyProductException as exc:
        return str(exc)
    return f"Покупка товара №{order.product_id} успешно оформлена, ID заказа: {order.id}"

