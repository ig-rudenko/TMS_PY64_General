numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

print(numbers)
print("Origin ID:", id(numbers))

#    0      1       2       3       4       5       6        7        8      9
# ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

# Не нужно включать в список сами себя. Это плохо для памяти и скорости.
# numbers.append(numbers)  # Лучше так не делать ❌❌❌❌


# Первые 5 элементов. Начиная с индекса 0 и до индекса 5. (5 не включительно)
short_numbers1 = numbers[0:5]  # Используй срезы
print(short_numbers1)
print("numbers[0:5] Short ID:", id(short_numbers1))

short_numbers2 = numbers[:5]  # Если не указать начальный индекс, то он будет равен 0 (5 не включительно)
print(short_numbers2)
print("numbers[:5] Short ID:", id(short_numbers2))

short_numbers3 = numbers[2:]  # От индекса 2 и до конца списка.
print(short_numbers3)
print("numbers[2:] Short ID:", id(short_numbers3))

short_numbers4 = numbers[1:-1]  # От второго элемента и до предпоследнего.

# Только нечетные элементы. От 0 до 10 с шагом 2.
steps1 = numbers[0:10:2]  # Второе число - это шаг.

print(steps1)
print("numbers[0:10:2] Short ID:", id(steps1))

# Только четные элементы. От 0 до 10 с шагом 2.
steps2 = numbers[1:10:2]  # Второе число - это шаг.

print(steps2)
print("numbers[1:10:2] Short ID:", id(steps2))

# Только четные элементы. От 0 до 10 с шагом 2. В ОБРАТНУЮ СТОРОНУ!
steps3 = numbers[-1:-10:-2]  # Второе число - это шаг.

print(steps3)
print("numbers[-1:-10:-2] Short ID:", id(steps3))

print(numbers[::-1])  # Выводит список в обратном порядке.
