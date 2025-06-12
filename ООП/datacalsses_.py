import sys


class UserGroup:
    def __init__(
        self,
        name: str,
        description: str
    ):
        self.name = name
        self.description = description


class Person:

    def __init__(
        self,
        name: str,
        age: int,
        email: str,
        first_name: str = "",
        last_name: str = "",
        is_superuser: bool = False,
        enabled: bool = True,
        groups: list[UserGroup] = None
    ):
        self.name = name
        self.age = age
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.is_superuser = is_superuser
        self.enabled = enabled

        if groups is None:
            self.groups = []
        else:
            self.groups = groups


admin_group = UserGroup(
    name="Admin",
    description="Admin group",
)

user_group = UserGroup(
    name="User",
    description="User group",
)

person = Person(
    name="John Doe",
    age=30,
    email="john.doe@example.com",
    first_name="John",
    last_name="Doe",
    is_superuser=True,
    enabled=True,
    groups=[
        admin_group,
        user_group,
    ]
)


print(sys.getsizeof(Person))  # 1712
print(sys.getsizeof(person))  # 48
# =====================================================

person.groups[0].name = "Admin"

print(person)