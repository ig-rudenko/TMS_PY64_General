NOTES = []

while True:
    print("""
###########################################
Привет в программу заметок!

Доступные действия:
1 - добавить заметку
2 - удалить заметку
0 - выйти
###########################################
""")

    if not NOTES:
        print('Нет заметок!')
    else:
        print('Все заметки:')
        for note in NOTES:
            print(f"""
        Заметка №{note['id']}:
        Заголовок: "{note['title']}"
        Дата: {note['date']}
        Текст: 
    {note['text']}
    """)
    action = input('Введите действие: ')

    if action == '1':
        title = input('Введите заголовок заметки: ')
        text = input('Введите текст заметки: ')
        date = input('Введите дату заметки: ')
        note = {
            'id': len(NOTES),
            'title': title,
            'text': text,
            'date': date
        }
        NOTES.append(note)
        print('Заметка добавлена!')

    elif action == '2':
        try:
            id_ = int(input('Введите id заметки: '))
        except ValueError:
            print('Введено неверное id!')
        else:
            try:
                NOTES.pop(id_)
            except IndexError:
                print('Заметки с таким id нет!')

    elif action == '0':
        break

    else:
        print('Неверное действие!')
