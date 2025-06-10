class CatSchema:
    tail = 1  # Атрибут класса

    def __init__(self, color, name="Tom", size=10, age=1):
        self.color = color  # Атрибут класса
        self.age = age  # Атрибут класса
        self.name = name  # Атрибут класса
        self.size = size  # Атрибут класса

    def get_full_stats(self):  # Метод класса
        return f"Цвет: {self.color} | Имя: {self.name} | Возраст: {self.age} | Размер: {self.size}"

    def say(self):
        return f"{self.name} мяукает"

    def sleep(self, seconds=0):
        return f"{self.name} спит {seconds} секунд"


class DogSchema:
    tail = 1  # Атрибут класса

    def __init__(self, color, name="Tom", size=10, age=1):
        self.color = color  # Атрибут класса
        self.age = age  # Атрибут класса
        self.name = name  # Атрибут класса
        self.size = size  # Атрибут класса

    def get_full_stats(self):  # Метод класса
        return f"Цвет: {self.color} | Имя: {self.name} | Возраст: {self.age} | Размер: {self.size}"

    def say(self):
        return f"{self.name} гавкает"

    def sleep(self, seconds=0):
        return f"{self.name} спит {seconds} секунд"


dog_white_1 = CatSchema(color="white")  # Создание экземпляра класса
cat_black_1 = CatSchema(color="black", name="Barsik")  # Создание экземпляра класса
cat_orange_1 = CatSchema(color="orange", name="Murzik", age=5)  # Создание экземпляра класса

print(cat_black_1.tail)

print(dog_white_1.get_full_stats())
print(dog_white_1.say())
