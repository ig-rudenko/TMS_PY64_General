import uuid


class SubjectsError(Exception):
    pass


class Person:
    def __init__(self, name, age):
        self.name = name
        self.user_id = str(uuid.uuid4())
        self.age = age

    def __repr__(self) -> str:
        return self.name


class Student(Person):
    def __init__(self, name, age, course, group_id=None):
        super().__init__(name, age)
        self.course = course
        self.group_id = group_id
        self.__subjects = []

    @property
    def subjects(self):
        return self.__subjects

    def clear_subjects(self):
        self.__subjects.clear()

    def add_subject(self, subject):
        if not isinstance(subject, Subject):
            raise ValueError("Не является экземпляром класса Subject")
        if len(self.__subjects) <= 2 and subject not in self.__subjects:
            self.__subjects.append(subject)
        else:
            raise SubjectsError("Студент уже имеет 2 предмета или предмет уже есть в списке предметов")

    def remove_subject(self, subject):
        try:
            self.__subjects.remove(subject)
        except ValueError:
            pass


class Subject:
    def __init__(self, subject_name, time):
        self.subject_name = subject_name
        self.time = time


class Group:
    def __init__(self, group_name):
        self.group_id = str(uuid.uuid4())
        self.group_name = group_name
        self.__students = []
        self.__subjects = []

    @property
    def students(self):
        return self.__students

    def clear_students(self):
        self.__students.clear()

    def add_student(self, *students):
        for student in students:
            if not isinstance(student, Student):
                continue
            self.__students.append(student)
            student.group_id = self.group_id

    def remove_student(self, student):
        try:
            self.__students.remove(student)
        except ValueError:
            pass


python_group = Group("Python11")

st1 = Student("Anna", 30, "Python")
st2 = Student("Boris", 31, "Python")
st3 = Student("Olga", 32, "Python")

print(python_group.students)
python_group.add_student(st1, st2, st3)

print(python_group.students)
