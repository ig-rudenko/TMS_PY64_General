import uuid


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.user_id = str(uuid.uuid4())

        self.check_age(age)
        self.age = age

    @staticmethod
    def check_age(age: int) -> None:
        if age <= 0 or age > 120:
            raise ValueError("Некорректный возраст")

    def __repr__(self) -> str:
        return self.name

    @classmethod
    def parse_data(cls, data: str):
        username, age = data.split(",")
        return cls(username, int(age))


class Student(Person):
    def __init__(self, name: str, age: int, course: int = "1", group_id: str | None = None):
        super().__init__(name, age)
        self.course = course
        self.group_id = group_id


p = Person.parse_data("John, 20")
st = Student.parse_data("John, 20")

print(p.__class__)
print(st.__class__)