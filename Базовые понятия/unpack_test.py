# РАСПАКОВКИ

x = 1
y = 0

# Распаковка кортежа.
# x, y = tuple(y, x)
# tuple(x, y) = tuple(y, x)
x, y = y, x


list1 = list("abcd")

# `*all_but_last` - Переменная, которая будет хранить все элементы, кроме последнего.
# `last` - Переменная, которая будет хранить последний элемент.
*all_but_last, last = list1
# all_but_last, last = list1[:-1], list1[-1]  # Можно записать также как.

print(all_but_last)
print(last)

first, *all_but_first = list1
# first, all_but_first = list1[0], list1[1:]  # Можно записать также как.

print(first)  # Элемент list1[0].
print(all_but_first)  # type - Список.


# Так как в списке 4 элемента, то в `middle` будет пустой список.
tre, some_var, *middle, pre_last, last = list1
print(tre)
print(some_var)
print(middle)
print(pre_last)
print(last)
