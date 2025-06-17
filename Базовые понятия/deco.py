
def simple_decorator(func):

    def wrapper(*args, **kwargs):
        print("Начало выполнения функции")
        res = func(*args, **kwargs)  # Вызываем переданную функцию и сохраняем результат
        print("Конец выполнения функции")
        return res

    return wrapper


@simple_decorator
def longest_word(text):
    print("Функция найдет самое длинное слово в предложении")
    return max(text.split(), key=len)


@simple_decorator
def sum_abc(a, b, c):
    return a + b + c


@simple_decorator
def print_text():
    print("Текст")

longest_word = simple_decorator(longest_word)

print(sum_abc(1, 2, 3))
print(longest_word("123"))
