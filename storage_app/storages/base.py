from abc import ABC, abstractmethod

from ..types import NoteSchema


class AbstractStorage(ABC):

    @abstractmethod
    def add_note(self, note: NoteSchema) -> None:
        pass

    @abstractmethod
    def delete_note(self, id_: int) -> bool:
        pass

    @abstractmethod
    def get_all_notes_verbose(self) -> str:
        pass
