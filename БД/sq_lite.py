import sqlite3

create_user_table = """
create table if not exists users (
	id INTEGER PRIMARY KEY autoincrement,
	username varchar(64) unique not null,
    password varchar(64) not null,
    phone varchar(20) null
);
"""

database = sqlite3.connect("users.db")  # Это создаст файл users.db, если его нет

database.execute(create_user_table)  # Выполняем запрос


def add_user(username, password, phone):
    database.execute(
        "insert into users (username, password, phone) values (?, ?, ?)",
        (username, password, phone),
    )
    database.commit()


def show_users():
    for user in database.execute("select username, password from users"):
        print(type(user), user)


try:
    add_user("user1", "pass1", "1234567890"),
    add_user("user2", "pass2", "1234567891"),
except sqlite3.IntegrityError:
    print("Users already exists")
show_users()
