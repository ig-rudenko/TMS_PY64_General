import random
from abc import ABC, abstractmethod


class BaseAnimal(ABC):  # Абстрактный класс, который не может быть использован напрямую
    tail = 1  # Атрибут класса

    def __init__(self, color, name, size, age):
        self.color = str(color)  # Атрибут класса
        self.age = abs(age)  # Атрибут класса
        self.name = str(name)  # Атрибут класса
        self.size = size  # Атрибут класса

        self.__dna = self.__generate_dna()  # "Защищенный" атрибут класса, не используйте его вне класса, пожалуйста.

    def get_dna(self):  # Getter
        return self.__dna.upper()

    def set_dna(self, dna):  # Setter
        if dna in ["Atg", "Gta", "Gat"]:
            self.__dna = dna

    @property
    def dna(self) -> str:  # Getter
        print("Получение атрибута __dna")
        return self.__dna.upper()

    @dna.setter
    def dna(self, value: str):  # Setter
        print("Установка атрибута __dna")
        if value in ["Atg", "Gta", "Gat"]:
            self.__dna = value
        else:
            print("Неверное значение DNA")

    def __generate_dna(self):  # Приватный метод класса не наследуются!
        return random.choice(["Atg", "Gta", "Gat"])

    def get_full_stats(self):  # Метод класса
        return f"Цвет: {self.color} | Имя: {self.name} | Возраст: {self.age} | Размер: {self.size}"

class FlyingMixin(ABC):  # Абстрактный класс, который не может быть использован напрямую

    @abstractmethod  # Абстрактный метод, который должен быть переопределен в дочерних классах
    def fly(self):
        pass

    def move(self):
        self.fly()

class BasicActionsMixin(ABC):  # Абстрактный класс, который не может быть использован напрямую

    def sleep(self, seconds=1):
        print("Спим", self.__class__, "BasicActionsMixin")
        return f"{self.name} спит {seconds} секунд"

    @abstractmethod  # Абстрактный метод, который должен быть переопределен в дочерних классах
    def say(self):  # Переопределение метода родительского класса BaseAnimal
        pass

    @abstractmethod  # Абстрактный метод, который должен быть переопределен в дочерних классах
    def eat(self, food):
        pass

    @abstractmethod  # Абстрактный метод, который должен быть переопределен в дочерних классах
    def move(self):
        pass


class Cat(BaseAnimal, BasicActionsMixin):  # Наследование класса BaseAnimal

    def __init__(self, color, name="Tom", size=10, age=1, tail=2):
        super().__init__(color, name, size, age)
        self.cat_name = name  # Атрибут экземпляра класса

    def eat(self, food):
        pass

    def move(self):
        pass

    def say(self):  # Переопределение метода родительского класса BaseAnimal
        super().say()
        return f"{self.name} мяукает"


class Dog(BaseAnimal, BasicActionsMixin):  # Наследование класса BaseAnimal

    def eat(self, food):
        pass

    def move(self):
        pass

    def say(self):
        return f"{self.name} гавкает"


class Fish(BaseAnimal, BasicActionsMixin):  # Наследование класса BaseAnimal
    tail = 2  # Атрибут класса

    def move(self):
        pass

    def eat(self, food):
        pass

    def say(self):
        return f"{self.name} молчит"


class Bird(BaseAnimal, FlyingMixin, BasicActionsMixin):  # Наследование класса BaseAnimal

    def fly(self):
        print("Летим")

    def say(self):
        pass

    def eat(self, food):
        pass



bird1 = Bird("Red", "Bird1", 10, 1)
bird1.sleep(1)

bird1.fly()
bird1.move()
