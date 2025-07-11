from dataclasses import dataclass


@dataclass
class Note:
    title: str
    text: str
    date: str
    id_: int = 0


class NotesStorage:

    def __init__(self):
        self._notes: list[Note] = []

    def add_note(self, note: Note) -> None:
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
            return 'Нет заметок!'

        text = 'Все заметки:'
        for note in self._notes:
            text += f"""
    Заметка №{note.id_}:
    Заголовок: "{note.title}"
    Дата: {note.date}
    Текст: 
{note.text}
    """
        return text


class Menu:

    def __init__(self, storage: NotesStorage):
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
        if action == '1':
            self.add_note()
            return 'Заметка успешно добавлена!'
        elif action == '2':
            return self.delete_note()
        elif action == '0':
            raise SystemExit("Программа завершена!")

        raise ValueError('Неверное действие!')

    def add_note(self) -> None:
        title = input('Введите заголовок заметки: ')
        text = input('Введите текст заметки: ')
        date = input('Введите дату заметки: ')

        note = Note(title=title, text=text, date=date)
        self._storage.add_note(note)

    def delete_note(self) -> str:
        try:
            id_ = int(input('Введите id заметки: '))
        except ValueError:
            return 'Неверный id заметки!'
        deleted = self._storage.delete_note(id_)
        if deleted:
            return 'Заметка успешно удалена!'
        else:
            return 'Заметка не найдена!'

    def run(self):
        while True:
            print(self.welcome())
            action = input('Введите действие: ')
            try:
                result = self.process_action(action)
                print(result)
            except ValueError as e:
                print(e)


note_storage = NotesStorage()
menu = Menu(note_storage)
menu.run()
