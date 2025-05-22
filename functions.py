words = ["Первое слово", 1, "Второе слово", "Третье слово", "Четвертое слово"]

new_words = [1, 2, 3]


def test_func():
    return "TEST"


# Объявляем функцию с 1 аргументом.
# ФУНКЦИЯ САМА НЕ ЗАПУСКАЕТСЯ, ЕЕ НАДО ВЫЗВАТЬ!
def format_list_to_lower_text(any_list, make_str=True):
    """Принимает любой список и возвращает список строк этих элементов, в нижнем регистре."""
    new_words = []

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

print(words2)
print(format_list_to_lower_text)
print(format_list_to_lower_text(words2, True))
