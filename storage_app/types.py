from dataclasses import dataclass


@dataclass
class Note:
    title: str
    text: str
    date: str
    id_: int = 0
