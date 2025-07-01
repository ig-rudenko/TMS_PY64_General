from .storages import AbstractStorage
from .types import NoteSchema


class Menu:

    def __init__(self, storage: AbstractStorage):
        self._storage = storage

    @staticmethod
    def welcome() -> str:
        return """
###########################################
    Привет в программу заметок!

    Доступные действия:
    1 - добавить заметку
    2 - удалить заметку
    0 - выйти
###########################################
    """

    def process_action(self, action: str) -> str:
        if action == "1":
            self.add_note()
            return "Заметка успешно добавлена!"
        elif action == "2":
            return self.delete_note()
        elif action == "0":
            raise SystemExit("Программа завершена!")

        raise ValueError("Неверное действие!")

    def add_note(self) -> None:
        title = input("Введите заголовок заметки: ")
        text = input("Введите текст заметки: ")
        date = input("Введите дату заметки: ")

        note = NoteSchema(title=title, text=text, date=date)
        self._storage.add_note(note)

    def delete_note(self) -> str:
        try:
            id_ = int(input("Введите id заметки: "))
        except ValueError:
            return "Неверный id заметки!"
        deleted = self._storage.delete_note(id_)
        if deleted:
            return "Заметка успешно удалена!"
        else:
            return "Заметка не найдена!"

    def run(self):
        while True:
            print(self.welcome())
            print(self._storage.get_all_notes_verbose())
            action = input("Введите действие: ")
            try:
                result = self.process_action(action)
                print(result)
            except ValueError as e:
                print(e)
