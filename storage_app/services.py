from sqlalchemy import select

from .database import session_maker
from .models import Note, User
from .types import NoteSchema


def create_user(username: str, password: str, email: str) -> User:
    with session_maker() as session:
        user = User(username=username, password=password, email=email)
        session.add(user)
        session.commit()
        session.refresh(user)

    return user


def create_user_from_input() -> User:
    if input("Do you want to create a new user? (y/n): ").lower() == "y":
        username = input("Enter username: ")
        password = input("Enter password: ")
        email = input("Enter email: ")
        return create_user(username, password, email)
    else:
        username = input("Enter username: ")
        with session_maker() as session:
            user = session.query(User).filter(User.username == username).first()
            if user is None:
                raise ValueError(f"User with username {username} not found")
            return user


def get_note(note_id: int) -> Note:
    with session_maker() as session:
        note = session.get(Note, note_id)
        if note is None:
            raise ValueError(f"Note with id {note_id} not found")

        return note


def get_notes(user_id: int | None = None, limit: int | None = 5, offset: int | None = 0) -> list[NoteSchema]:
    with session_maker() as session:
        query = (
            select(Note.title, Note.created_at, Note.content, User.username, User.email)
            .limit(limit)
            .offset(offset)
            .outerjoin(Note.user)
        )
        if user_id:
            query = query.where(Note.user_id == user_id)

        result = session.execute(query).all()

        obj_list = []
        for note in result:
            obj_list.append(
                NoteSchema(
                    title=note[0],
                    date=note[1],
                    text=note[2],
                    username=note[3],
                )
            )
        return obj_list


def create_note(title: str, content: str, user_id: int) -> Note:
    with session_maker() as session:
        note = Note(title=title, content=content, user_id=user_id)
        session.add(note)
        session.commit()
        session.refresh(note)

    return note


def update_note(note_id: int, title: str, content: str) -> Note:
    with session_maker() as session:
        note = session.get(Note, note_id)
        if note is None:
            raise ValueError(f"Note with id {note_id} not found")

        note.title = title
        note.content = content
        session.commit()
        session.refresh(note)

    return note


def delete_note(note_id: int) -> None:
    with session_maker() as session:
        session.query(Note).filter(Note.id == note_id).delete()
        session.commit()
