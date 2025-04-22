import os


def create_file():
    with open("notes.txt", "w") as f:
        pass  # Создание (очистка) файла
    print("Файл 'notes.txt' создан и очищен.")


def add_note():
    note = input("Введите текст заметки: ")
    with open("notes.txt", "a") as f:
        f.write(note + "\n")
    print("Заметка добавлена.")


def view_notes():
    if not os.path.exists("notes.txt"):
        print("Файл не найден. Сначала создайте файл.")
        return

    with open("notes.txt", "r") as f:
        notes = f.readlines()
        if not notes:  # Если файл пуст
            print("Файл пуст.")
            return

        for index, note in enumerate(notes, start=1):
            print(f"{index}: {note.strip()}")  # Выводим заметки с порядковыми номерами


def main():
    while True:
        command = input("Введите команду (create, add, view, exit): ").strip().lower()

        if command == "create":
            create_file()
        elif command == "add":
            add_note()
        elif command == "view":
            view_notes()
        elif command == "exit":
            print("Выход из программы.")
            break
        else:
            print("Некорректная команда. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()