import math
from functools import total_ordering
from typing import Hashable


@total_ordering
class Coordinate:
    __slots__ = ['_x', '_y']  # Позволяет ограничить количество атрибутов класса.

    def __init__(self, x: int | float, y: int | float):
        self._x = x
        self._y = y

    def __repr__(self) -> str:
        return f"Coordinate({self._x}, {self._y})"

    def __bool__(self) -> bool:
        return bool(self._x and self._y)

    def __len__(self) -> int:
        return int(math.sqrt(self._x ** 2 + self._y ** 2))

    @property
    def pair(self) -> tuple[int | float, int | float]:
        return self._x, self._y

    @property
    def length(self) -> float:
        return math.sqrt(self._x ** 2 + self._y ** 2)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Координата должна быть числом.")
        else:
            self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Координата должна быть числом.")
        else:
            self._y = value

    def __add__(self, other):
        """
        Вызывается, когда мы добавляем к нашему объекту что-то.
        :param other: Это может быть что угодно.
        """
        if not isinstance(other, Coordinate):
            raise TypeError("Нельзя складывать координаты с чем-то, что не является координатой.")
        return Coordinate(
            self._x + other._x,
            self._y + other._y
        )

    def __radd__(self, other):
        """
        Вызывается, когда мы добавляем наш объект к чему-то.
        :param other: Это может быть что угодно.
        """
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        """
        Вызывается, когда мы вычитаем из нашего объекта что-то.
        :param other:
        :return:
        """
        if not isinstance(other, Coordinate):
            raise TypeError("Нельзя складывать координаты с чем-то, что не является координатой.")
        return Coordinate(
            self._x - other._x,
            self._y - other._y
        )

    def __rsub__(self, other):
        return self.__sub__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Нельзя умножать координаты на что-то, что не является числом.")
        return Coordinate(
            self._x * other,
            self._y * other
        )

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Нельзя умножать координаты на что-то, что не является числом.")
        return Coordinate(
            self._x / other,
            self._y / other
        )

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def __itruediv__(self, other):
        return self.__truediv__(other)

    # ====================== СРАВНЕНИЕ ======================

    def __gt__(self, other):  # > (больше)
        if not isinstance(other, Coordinate):
            raise TypeError("Нельзя сравнивать координаты с чем-то, что не является координатой.")
        return self.length > other.length

    def __eq__(self, other):  # == (равно)
        if not isinstance(other, Coordinate):
            raise TypeError("Нельзя сравнивать координаты с чем-то, что не является координатой.")
        else:
            return self._x == other._x and self._y == other._y

    def __neg__(self):  # - (отрицание)
        return Coordinate(-self._x, -self._y)

    def __hash__(self) -> Hashable:
        if self._x == 0 and self._y == 0:
            return 0
        else:
            return hash((self._x, self._y))

    def __abs__(self):
        return Coordinate(
            abs(self._x),
            abs(self._y),
        )


z = Coordinate(0, 0)
c1 = Coordinate(1, 2)
c2 = Coordinate(3, -4)

print(z.pair)
if not z:
    print("Координата нулевая.")

print(len(c2))

if c1 <= c2:
    print("Координата 1 больше координаты 2.")
else:
    print("Координата 2 больше координаты 1.")

print(-c1)

coods = {c1, c2}

print(coods)

print(hash(c1))
print(hash(c2))

