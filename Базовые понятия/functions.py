words = ["Первое слово", 1, "Второе слово", "Третье слово", "Четвертое слово"]

new_words = [1, 2, 3]


def test_func():
    return "TEST"


# Объявляем функцию с 1 аргументом.
# ФУНКЦИЯ САМА НЕ ЗАПУСКАЕТСЯ, ЕЕ НАДО ВЫЗВАТЬ!
def format_list_to_lower_text(any_list: list, make_str: bool = True) -> list[str]:
    """Принимает любой список и возвращает список строк этих элементов, в нижнем регистре."""
    new_words: list[str] = []

    for element in any_list:
        if not isinstance(element, str) and make_str:
            new_words.append(str(element).lower())

        elif isinstance(element, str):
            new_words.append(element.lower())

    new_words.append(test_func())

    # return возвращает значение и мгновенно завершает работу функции!
    # Если нет return, то функция вернет None.
    # Если return без значения, то вернет None и мгновенно завершает работу функции!
    return new_words


words2 = ["Первое слово", 1231231231, "Второе слово", "Третье слово", "Четвертое слово"]

# Нужно создать новый список, в котором слова будут в нижнем регистре.
words33 = ["Первое слово", 1, "Второе слово", "Третье слово", "Четвертое слово"]

ff = format_list_to_lower_text

print(ff(words33, False))  # Позиционные аргументы

# Именованные аргументы, всегда идут после позиционных аргументов!
print(ff(any_list=words33, make_str=False))
print(ff(make_str=False, any_list=words33))

# ===================================================================================================================


# Нужно создать новый список, в котором слова будут в нижнем регистре.
words33 = ["Первое слово", 1, "Второе слово", "Третье слово", "Четвертое слово"]

# Преобразование всех элементов списка в строчки
r1 = map(str, words33)  # Это не результат работы функции, а объект, который нужно превратить в список
# В нижний регистр.
r2 = map(str.lower, r1)

new_list = list(map(str.lower, map(str, words33)))
print(new_list)


# Фильтруем только строки
# В нижний регистр.

def is_str(element) -> bool:
    return isinstance(element, str)


r1 = filter(is_str, words33)
r2 = map(str.lower, r1)

new_list = list(map(str.lower, filter(is_str, words33)))
print(new_list)

# Лямбда функция (анонимная функция)

# Фильтруем только строки
# В нижний регистр.
r1 = filter(lambda x: isinstance(x, str), words33)
r2 = map(str.lower, r1)

new_list = list(map(str.lower, filter(lambda x: isinstance(x, str), words33)))
print(new_list)

# ------------------------------------------------------------------------------------------------------------------

# new_list = []
# for x in words33:
#     new_list.append(x.lower())

# Либо так
# new_list = [x.lower() for x in words33]
# print(new_list)


# new_list = []
# for x in words33:
#     if isinstance(x, str):
#         new_list.append(x.lower())

# Либо так
new_list = [x.lower() for x in words33 if isinstance(x, str)]
print(new_list)

# new_dict = {}
# for x in text:
#     new_dict[x] = text.count(x)

# Либо так
text = "Python генерирует псевдослучайное целое число из заданного диапазона"
new_dict = {x: text.count(x) for x in text}

print(new_dict)

reviews = [
    {
        "reviewId": 501,
        "userId": 101,
        "username": "techguy123",
        "rating": 5,
        "comment": "Amazing sound quality and battery life!"
    },
    {
        "reviewId": 502,
        "userId": 102,
        "username": "jane_doe",
        "rating": 4,
        "comment": "Great headphones but a bit pricey."
    }
]


top = (x for x in reviews if x["rating"] == 5)  # Это будет генератор, а не список! (Не кортеж!)
# Ленивый объект, будет выполнен только тогда, когда мы обратимся к его значениям.

print(top)

def id_generator(start: int, step: int = 1):
    start -= 1

    def generate():
        nonlocal start
        start += step
        return start

    return generate

generator = id_generator(start=1, step=2)

print(generator())
print(generator())
print(generator())
print(generator())
print(generator())
print(generator())