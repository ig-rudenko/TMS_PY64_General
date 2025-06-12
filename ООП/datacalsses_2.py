import sys
from dataclasses import dataclass, field


@dataclass
class UserGroup:
    name: str
    description: str


@dataclass
class Person:
    name: str
    age: int
    email: str
    first_name: str = ""
    last_name: str = ""
    is_superuser: bool = False
    enabled: bool = True
    groups: list[UserGroup] = field(default_factory=list)


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
