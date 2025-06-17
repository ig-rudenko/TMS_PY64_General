user_input = input("Введите что-то: ")  # Пауза и ввод числа пользователем

user_input = user_input.strip()  # Убираем пробелы в начале и конце строки

print("Длина строки:", len(user_input))

#            0             1        2  3
list_ = [user_input, "some_string", 3, 5]

# Ниже одинаковые проверки
is_digit = list_[0].isdigit()  # Вызов метода () для проверки на то, что ввели число
# is_digit = user_input.isdigit()  # Проверка на то, что ввели число


print("is_digit:", is_digit)

# Создается ДРУГАЯ строчка, потому что строка неизменяемый тип данных
user_input = user_input.replace(".", "")  # Убираем точку

print("new_str:", user_input)

user_input = user_input.upper()  # Переводим все в верхний регистр

print("new UPPER str:", user_input)

user_input = user_input.title()  # Переводим в заглавный регистр

print("new UPPER str:", user_input)

user_input = user_input.capitalize()  # Переводим первую букву в заглавный регистр

print("new capitalize str:", user_input)

# ✅ Возвращает список строчек
user_words = user_input.split()  # Разделяем строку на список по пробелам

print("Слов в строке:", len(user_words))

# Соединяем список строчек в одну строку через пробел
join_str = " ".join(user_words)

print("Соединенная строка:", join_str)

# ✅ Возвращает список строчек
text_parts = user_input.split(":")  # Разделяем строку на список по символу `:`

print("Слова в строке:", text_parts)

# Разделяем строку на список по символу `:` с конца и берем 1 элемент.
# Возвращает список строчек
text_parts = user_input.rsplit("\\", 2)

print("Слова в строке:", text_parts)

count_of_slashes = user_input.count("\\")  # Считаем количество символов `\` в строке

print("Сколько символов `\\`:", count_of_slashes)


print("Первая буква в строке:", user_input[0])  # Выбираем первую букву в строке


# user_input[0] = "A"  # ❌ Ошибка, так как строка неизменяемый тип данных
