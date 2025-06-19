list1 = ["apple", "banana", "cherry"]


def func(x):
    print("Работаю")
    return x.upper()


# Генераторное выражение
f_gen = (func(x) for x in list1)

for i in f_gen:
    print("В цикле!", i)


# Генератор

print("Генератор")


def get_f_gen(array):
    print("Начинаю...")
    x = 1
    for f in array:
        print("Работаю!", x)
        yield str(f).upper()
        x += 1


f_gen = get_f_gen(list1)  # Создаем генератор
print(f_gen)

print("Выводим данные из генератора")

print(next(f_gen))
print(next(f_gen))

f_gen = get_f_gen([1, 2, 3])

for i in f_gen:
    print("В цикле!", i)
