from .base import AbstractStorage
from ..database import Base, engine
from ..services import create_note, delete_note, get_notes
from ..types import NoteSchema
from ..models import User, Note as NoteModel


class DBStorage(AbstractStorage):

    def __init__(self, user: User):
        self._user = user

    def add_note(self, note: NoteSchema) -> None:
        create_note(note.title, note.text, self._user.id)

    def delete_note(self, id_: int) -> bool:
        delete_note(id_)
        return True

    def get_all_notes_verbose(self) -> str:
        text = ""
        for note in get_notes(limit=None, offset=None):
            text += f"""
Название: {note.title}
    Дата создания: {note.date}
    Пользователь: {note.username}
Содержание: {note.text}
"""
        return text
