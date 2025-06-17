import json
from pathlib import Path

from app.storages.memory import NotesMemoryStorage
from app.types import Note


class NotesJSONFileStorage(NotesMemoryStorage):
    def __init__(self, file_path: str):
        super().__init__()
        self._file_path = file_path
        self.__load()

    def __load(self) -> None:
        try:
            with open(self._file_path, 'r', encoding='utf-8') as file:
                self._notes = [Note(**data) for data in json.load(file)]
        except FileNotFoundError:
            Path(self._file_path).touch()

    def __save(self) -> None:
        with open(self._file_path, 'w', encoding='utf-8') as file:
            json.dump([note.__dict__ for note in self._notes], file, ensure_ascii=False)

    def add_note(self, note: Note) -> None:
        super().add_note(note)
        self.__save()

    def delete_note(self, id_: int) -> bool:
        is_deleted = super().delete_note(id_)
        if is_deleted:
            self.__save()
        return is_deleted
