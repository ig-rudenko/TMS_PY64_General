from storage_app.models import User, Note
from storage_app.database import Base, engine
from storage_app.menu import Menu
from storage_app.services import create_user, create_user_from_input
from storage_app.storages import NotesMemoryStorage, NotesJSONFileStorage, DBStorage


print(Note, User)
Base.metadata.create_all(engine)

user = create_user_from_input()

note_storage = DBStorage(user)

menu = Menu(note_storage)
menu.run()
