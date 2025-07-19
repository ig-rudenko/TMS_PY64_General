from models import Note
from settings import db


def create_note(user_id: int, title: str, content: str) -> Note:
    note = Note(title=title, content=content, user_id=user_id)
    db.session.add(note)
    db.session.commit()
    return note
