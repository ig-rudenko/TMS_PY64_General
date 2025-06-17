from storage_app.menu import Menu
from storage_app.storages import NotesMemoryStorage, NotesJSONFileStorage

env = "dev"
if env == "dev":
    note_storage = NotesMemoryStorage()
else:
    note_storage = NotesJSONFileStorage("notes.json")

menu = Menu(note_storage)
menu.run()
