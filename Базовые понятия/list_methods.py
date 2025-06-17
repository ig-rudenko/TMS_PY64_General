#            0      1       2       3       4       5       6        7        8      9
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]


#    0      1       2       3       4       5       6        7        8      9       10
# ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

# Добавляет элемент в список по указанному индексу
numbers.insert(0, "zero")

# Возвращает индекс первого элемента, равного указанному значению
match = numbers.index("five")

print(match)

# Возвращает количество элементов, равных указанному значению
numbers.count("five")

# Удаляет первый элемент, равный указанному значению
numbers.remove("five")

# Возвращает последний элемент из списка и удаляет его
number1 = numbers.pop()

print(numbers)

# Возвращает элемент по указанному индексу и удаляет его
number2 = numbers.pop(0)

print(numbers)

# МЕТОДЫ ИЗМЕНЯЮТ САМ СПИСОК, НЕ ВОЗВРАЩАЮТ НОВЫЙ ❗️

# Добавляет элемент в конец списка
numbers.append("eleven")

# Сортирует список по возрастанию
numbers.sort()

# Разворачивает список наоборот
numbers.reverse()
