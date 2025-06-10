class NonPositiveInt(ValueError):  # Создаем класс исключения
    pass


class PosInt(int):

    def __init__(self, n):
        n = int(n)
        if n <= 0:
            raise NonPositiveInt('Должно быть положительное число')


n = PosInt(5)

print(n)