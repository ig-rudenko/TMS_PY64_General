import random


class BaseAnimal:
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

    def sleep(self, seconds=1):
        self.say()
        return f"{self.name} спит {seconds} секунд"

    def say(self):  # Переопределение метода родительского класса BaseAnimal
        print("Я не умею говорить")


class Cat(BaseAnimal):  # Наследование класса BaseAnimal

    def __init__(self, color, name="Tom", size=10, age=1, tail=2):
        super().__init__(color, name, size, age)
        self.cat_name = name  # Атрибут экземпляра класса

    def say(self):  # Переопределение метода родительского класса BaseAnimal
        super().say()
        return f"{self.name} мяукает"


class Dog(BaseAnimal):  # Наследование класса BaseAnimal

    def say(self):
        return f"{self.name} гавкает"


class Fish(BaseAnimal):  # Наследование класса BaseAnimal
    tail = 2  # Атрибут класса

    def say(self):
        return f"{self.name} молчит"


dog_white_1 = Cat(color="white")  # Создание экземпляра класса
cat_black_1 = Cat(color="black", name="Barsik")  # Создание экземпляра класса
cat_orange_1 = Cat(color="orange", name="Murzik", age=5)  # Создание экземпляра класса

# print(cat_orange_1)

print(cat_black_1.get_dna())
# cat_black_1.set_dna("Atg")
cat_black_1.dna = "345"
print(cat_black_1.dna)

# print(cat_orange_1)  # Не используйте так, пожалуйста! (Хак приватных атрибутов)

# print(dog_white_1.get_full_stats())
print(dog_white_1.say())
