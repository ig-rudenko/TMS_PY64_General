var1 = int(input("enter a number 1: "))
var2 = int(input("enter a number 2: "))

# if var == 0:
#     print("it is zero")
# else:
#     if var > 0:
#         print("it is a positive number")
#     else:
#         print("it is a negative number")

if var1 < 0:
    print("number 1 is a negative number")
elif var1 > 0:
    print("number 1 is a positive number")
else:
    print("number 1 is zero")


# Логическое И
#    1       *      0     =    0
if var1 < 0 and var2 < 0:
    print("both are negative numbers")


# Логическое ИЛИ
#   0       +      1     =    1
if var1 > 0 or var2 > 0:
    print("at least one of them is positive")


if (var1 < 0 or var2 < 0) and var1 != var2:
    print("one of them is negative and they are not equal")


list_1 = [1]


# ДЛЯ AND.
# Пока первое выражение ложь, то второе не выполняется.
if len(list_1) > 0 and list_1[0] < 0:  # True and False = False
    print("AND CHECK Первый элемент меньше нуля")
elif len(list_1) == 0:  # False
    print("AND CHECK Список пуст")
else:  # Anyway
    print("AND CHECK Первый элемент больше нуля")


# ДЛЯ OR.
# Пока первое выражение истинно, то второе не выполняется.
if len(list_1) > 0 or list_1[0] < 0:  # True or False = True
    print("OR CHECK Первый элемент меньше нуля")   # ---
elif len(list_1) == 0:  # Пропускаем, т.к. предыдущее выражение истинно.
    print("OR CHECK Список пуст")
else:  # Пропускаем, т.к. предыдущее выражение истинно.
    print("OR CHECK Первый элемент больше нуля")

# list_1 = [1]

# AND выполняется раньше, чем OR.
# Решающее значение остается за OR.

list_1 = [22]

if len(list_1) > 0 and (list_1[0] < 0 or list_1[0] > 10):  # (True and False) or True = True
    print("COMPLEX CHECK Первый элемент такой как надо.")   # ---
elif len(list_1) == 0:  # Пропускаем, т.к. предыдущее выражение истинно.
    print("COMPLEX CHECK Список пуст")
else:  # Пропускаем, т.к. предыдущее выражение истинно.
    print("COMPLEX CHECK Первый элемент не такой как надо.")



# if result:
# if bool(result):  # Поведение bool определяется классом объекта `result`.

# if bool(len(result) > 0):  # Поведение для list, str, tuple, dict, set.
# if bool(result != 0):  # Поведение для int, float, complex.
# if bool(None != None):  # Поведение для None. Всегда False.

# if bool(True):
# if True:

result = []

is_empty = not bool(result)

if result:   # Подразумеваем - len(result) != 0:
    print("result is not empty")


user = None
# user = {}

if user is not None:  # Если объект не является None.
    print("Имеем пользователя")
else:
    print("Нет пользователя")

if user is None:  # Если объект является None.
    print("Нет пользователя")
else:
    print("Имеем пользователя")


x = 34

# ВСЕГДА нужно указывать else!
answer = "Четное число" if x % 2 == 0 else "Не четное число"


user = {
    "name": "John",
    "age": None,
}

# Упрощаем до:
# user["age"] = user["age"] if user["age"] is not None else -1
# user["age"] = user["age"] if user["age"] else -1


# Пока первое выражение истинно, то второе не присваивается.
user["age"] = user["age"] or -1
print(user)

# Пока первое выражение ложь, то второе не присваивается.
# Если первое выражение истинно, то второе присваивается.
user["age"] = user["age"] and 0
print(user)
