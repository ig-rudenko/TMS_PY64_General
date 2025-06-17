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
        print('Заметка успешно добавлена!')

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


note_storage = NotesStorage()

while True:
    print(note_storage.get_all_notes_verbose())
    print("""
###########################################
Привет в программу заметок!

Доступные действия:
1 - добавить заметку
2 - удалить заметку
0 - выйти
###########################################
""")
    action = input('Введите действие: ')
    if action == '1':
        title = input('Введите заголовок заметки: ')
        text = input('Введите текст заметки: ')
        date = input('Введите дату заметки: ')

        note = Note(title=title, text=text, date=date)
        note_storage.add_note(note)

    elif action == '2':
        try:
            id_ = int(input('Введите id заметки: '))
        except ValueError:
            print('Неверный id заметки!')
            continue

        deleted = note_storage.delete_note(id_)
        if deleted:
            print('Заметка успешно удалена!')
        else:
            print('Заметка не найдена!')

    elif action == '0':
        break
    else:
        print('Неверное действие!')
