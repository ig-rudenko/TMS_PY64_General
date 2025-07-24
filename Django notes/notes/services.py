from django.contrib.auth import get_user_model

from notes.models import Note

User = get_user_model()  # Возвращает модель пользователя текущего проекта.

def create_user(username: str, email: str, password: str) -> User:
    return User.objects.create_user(username=username, email=email, password=password)


def create_note(title: str, content: str, user: User) -> Note:
    return Note.objects.create(title=title, content=content, user=user)
