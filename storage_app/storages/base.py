from abc import ABC, abstractmethod

from app.types import Note


class AbstractStorage(ABC):


    @abstractmethod
    def add_note(self, note: Note) -> None:
        pass

    @abstractmethod
    def delete_note(self, id_: int) -> bool:
        pass

    @abstractmethod
    def get_all_notes_verbose(self) -> str:
        pass