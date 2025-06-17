NOTES = []


def create_note(id_: int, title: str, text: str, date: str) -> dict:
    note = {
        'id': id_,
        'title': title,
        'text': text,
        'date': date
    }
    return note


def generate_id() -> int:
    return len(NOTES)


def add_note(note: dict) -> None:
    NOTES.append(note)
    print('Заметка успешно добавлена!')


def delete_note(id_: int) -> bool:
    try:
        NOTES.pop(id_)
        return True
    except IndexError:
        return False


def get_all_notes_verbose() -> str:
    if not NOTES:
        return 'Нет заметок!'

    text = 'Все заметки:'
    for note in NOTES:
        text += f"""
    Заметка №{note['id']}:
    Заголовок: "{note['title']}"
    Дата: {note['date']}
    Текст: 
{note['text']}
"""
    return text


while True:
    print(get_all_notes_verbose())
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

        note_id = generate_id()
        note = create_note(note_id, title, text, date)
        add_note(note)

    elif action == '2':
        try:
            id_ = int(input('Введите id заметки: '))
        except ValueError:
            print('Неверный id заметки!')
            continue

        deleted = delete_note(id_)
        if deleted:
            print('Заметка успешно удалена!')
        else:
            print('Заметка не найдена!')

    elif action == '0':
        break
    else:
        print('Неверное действие!')
