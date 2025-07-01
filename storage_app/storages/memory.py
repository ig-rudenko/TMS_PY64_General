from .base import AbstractStorage
from ..types import NoteSchema


class NotesMemoryStorage(AbstractStorage):

    def __init__(self):
        self._notes: list[NoteSchema] = []

    def add_note(self, note: NoteSchema) -> None:
        note.id_ = len(self._notes) + 1
        self._notes.append(note)

    def delete_note(self, id_: int) -> bool:
        try:
            self._notes.pop(id_)
            return True
        except IndexError:
            return False

    def get_all_notes_verbose(self) -> str:
        if not self._notes:
            return "Нет заметок!"

        text = "Все заметки:"
        for note in self._notes:
            text += f"""
    Заметка №{note.id_}:
    Заголовок: "{note.title}"
    Дата: {note.date}
    Текст: 
{note.text}
    """
        return text
