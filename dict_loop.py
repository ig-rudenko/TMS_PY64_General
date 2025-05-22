from pprint import pprint

user = {
    "userId": 2,
    "username": "janedoe",
    "email": "janedoe@example.com",
    "profile": {
        "firstName": "Jane",
        "lastName": "Doe",
        "birthDate": "1992-04-12",
        "gender": "female",
        "avatarUrl": "https://example.com/avatars/janedoe.jpg",
        "bio": "Digital marketer and blogger."
    },
}


# По умолчанию в цикле for проходимся только по ключам
for key in user:
    print("Ключ:", key, "Значение:", user[key])

# Можно указать напрямую проходиться по ключам
for key in user.keys():
    print("Ключ:", key, "Значение:", user[key])


# Проходимся только по значениям
for value in user.values():
    print("Значение:", value)


print("-" * 100)

# Возвращает последовательность кортежей, где каждый кортеж состоит из пары ключ-значение.
print(user.items())


# Проходимся по ключам и значениям
# Распаковка кортежа
# key, value = ('userId', 2)
for key, value in user.items():
    print("Ключ:", key, "Значение:", value)


some_list = [
    ['userId', 2],
    ['username', 'janedoe', 312, 0],
    ['email', 'janedoe@example.com', 312, 9, 0, 12, 234],
]

# Цикл прохода по списку с распаковкой значений вложенного списка.
for param, value, *other in some_list:
    print("param:", param, "value:", value, "other:", other)

# ---------------------------
# Вложенные списки
user = {
    "userId": None,
    "username": "janedoe",
    "email": "janedoe@example.com",
    "profile": {
        "firstName": "Jane",
        "lastName": "Doe",
        "birthDate": "1992-04-12",
        "gender": "female",
        "avatarUrl": "https://example.com/avatars/janedoe.jpg",
        "bio": "Digital marketer and blogger."
    },
}


flat_user = {}  # Пустой словарь для заполнения

# Нужно пройтись по всем параметрам пользователя (вложенным тоже).
for key, value in user.items():

    if isinstance(value, dict):
        for param, val in value.items():
            # Добавляем в новый словарь flat_user значение вложенного словаря по ключу,
            # состоящему из исходного ключа вложенного словаря и текущего ключа вложенного словаря
            new_key = key + "_" + param
            flat_user[new_key] = val
            print("Ключ:", key + "_" + param, "Значение:", val)

    else:
        flat_user[key] = value
        print("Ключ:", key, "Значение:", value)



flat_user = {}  # Пустой словарь для заполнения

# Нужно пройтись по всем параметрам пользователя (вложенным тоже).
for key, value in user.items():

    if value is None:
        print("Ключ:", key, "Значение:", value)
        print("BREAK")
        break  # Принудительно останавливает цикл. Сразу в конец цикла.

    if isinstance(value, list):
        # Пропускаем все значения словаря, если они являются списками.
        continue  # Переходим к следующему элементу.

    if isinstance(value, dict):
        for param, val in value.items():
            # Добавляем в новый словарь flat_user значение вложенного словаря по ключу,
            # состоящему из исходного ключа вложенного словаря и текущего ключа вложенного словаря
            new_key = key + "_" + param
            flat_user[new_key] = val
            print("Ключ:", key + "_" + param, "Значение:", val)
        continue  # Чтобы не выполнять код ниже, переходим к следующей итерации цикла.

    flat_user[key] = value
    print("Ключ:", key, "Значение:", value)
