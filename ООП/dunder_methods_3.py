import uuid


class SubjectsError(Exception):
    pass


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.user_id = str(uuid.uuid4())

        self.__check_age(age)
        self.age = age

    def __repr__(self) -> str:
        return self.name

    def __check_age(self, age: int) -> None:
        if age < 0 or age > 120:
            raise ValueError("Некорректный возраст")


class Student(Person):
    def __init__(self, name: str, age: int, course: str, group_id: str | None = None):
        super().__init__(name, age)
        self.course = course
        self.group_id = group_id
        self.__subjects: list[Subject] = []

    @property
    def subjects(self) -> list["Subject"]:
        return self.__subjects

    def clear_subjects(self) -> None:
        self.__subjects.clear()

    def add_subject(self, subject: "Subject") -> None:
        if not isinstance(subject, Subject):
            raise ValueError("Не является экземпляром класса Subject")
        if len(self.__subjects) <= 2 and subject not in self.__subjects:
            self.__subjects.append(subject)
        else:
            raise SubjectsError("Студент уже имеет 2 предмета или предмет уже есть в списке предметов")

    def remove_subject(self, subject: "Subject") -> None:
        try:
            self.__subjects.remove(subject)
        except ValueError:
            pass


class Subject:
    def __init__(self, subject_name: str, time: str):
        self.subject_name = subject_name
        self.time = time


class Group:
    def __init__(self, group_name: str):
        self.group_id = str(uuid.uuid4())
        self.group_name = group_name
        self.__students: list[Student] = []
        self.__subjects: list[Subject] = []
        self.__iter_start = 0

    @property
    def students(self) -> list[Student]:
        return self.__students

    def clear_students(self) -> None:
        self.__students.clear()

    def add_student(self, *students: Student) -> None:
        for student in students:
            if not isinstance(student, Student):
                raise ValueError("Должен быть студент")
            self.__students.append(student)
            student.group_id = self.group_id

    def remove_student(self, student: Student) -> None:
        try:
            self.__students.remove(student)
        except ValueError:
            pass

    def __iter__(self):
        self.__iter_start = -1
        return self

    def __next__(self):
        self.__iter_start += 1  # 3
        if self.__iter_start >= len(self.__students):
            raise StopIteration
        return self.__students[self.__iter_start]

    def __getitem__(self, item):
        if isinstance(item, (slice, int)):
            return self.__students[item]

        if isinstance(item, str):
            for student in self.__students:
                if student.name.lower() == item.lower():
                    return student
            return None

        raise IndexError("Некорректный индекс")

    # def __getattribute__(self, item: str):
    #     for student in object.__getattribute__(self, "_Group__students"):
    #         if student.name.lower() == item.lower():
    #             return student
    #     return super().__getattribute__(item)

    def __getattr__(self, item):
        for student in self.__students:
            if student.name.lower() == item.lower():
                return student
        return None


python_group = Group("Python11")

st1 = Student("Anna", 30, "Python")
st2 = Student("Boris", 31, "Python")
st3 = Student("Olga", 32, "Python")

print(python_group.__dict__)
print(python_group.__dir__())

print(python_group.students)
python_group.add_student(st1, st2, st3)

print(python_group.students)

for student in python_group:
    print(student)

# ==============================
iter_obj = iter(python_group)
while True:
    try:
        student = next(iter_obj)

        # ========================
        print(student)
        # ========================

    except StopIteration:
        break
# ==============================


st_anna = python_group["Anna"]

print(st_anna)


print(python_group.Anna.__class__)