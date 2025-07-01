from dataclasses import dataclass


@dataclass
class NoteSchema:
    title: str
    text: str
    date: str
    id_: int = 0
    username: str = ""
