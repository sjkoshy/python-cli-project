from peewee import *

db = PostgresqlDatabase("notes_app", user="notes_admin", password="notes_pass", host="localhost", port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class Note(BaseModel):
    title = CharField()
    content = TextField()

db.connect()
db.drop_tables([Note])
db.create_tables([Note])

Note(
    title="Grocery List",
    content="Milk, Eggs, Bread, Flour, Sugar"
).save()

Note(
    title="To Do",
    content="Clean, Homework, Laundry, Dishes"
).save()

Note(
    title="Reminders",
    content="Doctor's Appointment, Oil Change, Pay Bills"
).save()

Note(
    title="Places to Visit",
    content="New York, Paris, Tokyo, London, Rome"
).save()

Note(
    title="Books to Read",
    content="The Great Gatsby, The Odyssey, The Lord of the Rings, The Hobbit"
).save()

Note(
    title="Movies to Watch",
    content="The Godfather, The Shawshank Redemption, The Dark Knight, Star Wars"
).save()

def get_notes():
    return list(Note.select())

def get_note_by_id(id):
    return Note.get(Note.id == id)

def create_note():
    title = input("Enter a title: ")
    content = input("Enter the content: ")
    Note.create(
        title=title,
        content=content
    )
    print("Note created!")

def update_note():
    id = int(input("Enter the id of the note you want to update: "))
    try: 
        note = get_note_by_id(id)
        title = input("Enter a new title: ")
        content = input("Enter the new content: ")
        note.title = title
        note.content = content
        note.save()
        print("Note updated!")
    except DoesNotExist:
        print("Note not found!")

def delete_note():
    id = int(input("Enter the id of the note you want to delete: "))
    try: 
        note = get_note_by_id(id)
        note.delete_instance()
        print("Note deleted!")
    except DoesNotExist:
        print("Note not found!")

def list_notes():
    notes = get_notes()
    for note in notes:
        print(f"{note.id}: {note.title} - {note.content}")

def menu():
    while True:
        print("Notes App Menu")
        print("1. List notes")
        print("2. View note")
        print("3. Create a note")
        print("4. Update a note")
        print("5. Delete a note")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_notes()

        elif choice == "2":
            id = int(input("Enter the id of the note you want to view: "))
            try: 
                note = get_note_by_id(id)
                print(f"{note.id}: {note.title} - {note.content}")
            except DoesNotExist:
                print("Note not found!")
        elif choice == "3":
            create_note()
        elif choice == "4":
            update_note()
        elif choice == "5":
            delete_note()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

menu()