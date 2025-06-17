NOTES = []

def add_note(title, text, date):
    note = {
        'id': len(NOTES),
        'title': title,
        'text': text,
        'date': date
    }
    NOTES.append(note)
    print('Заметка добавлена!')
    return note


def delete_note(id_: int) -> bool:
    try:
        NOTES.pop(id_)
        return True
    except IndexError:
        print('Заметки с таким id нет!')
        return False


def show_all_notes():
    if not NOTES:
        print('Нет заметок!')
        return

    print('Все заметки:')
    for note in NOTES:
        print(f"""
    Заметка №{note['id']}:
    Заголовок: "{note['title']}"
    Дата: {note['date']}
    Текст: 
{note['text']}
""")


while True:
    show_all_notes()
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
        add_note(title, text, date)

    elif action == '2':
        id_ = int(input('Введите id заметки: '))
        delete_note(id_)

    elif action == '3':
        show_all_notes()

    elif action == '0':
        break
    else:
        print('Неверное действие!')
