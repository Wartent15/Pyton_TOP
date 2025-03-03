
filename = "notes.txt"

while True:
    print("\nВыберите действие:")
    print("  create - Создать новый файл")
    print("  add - Добавить заметку")
    print("  view - Просмотреть заметки")
    print("  exit - Выйти из программы")

    choice = input("Введите команду: ").lower()

    if choice == "create":
        try:
            with open(filename, "w") as f:
                pass  # Просто создаем/очищаем файл
            print(f"Файл '{filename}' создан и очищен.")
        except Exception as e:
            print(f"Ошибка при создании файла: {e}")

    elif choice == "add":
        try:
            with open(filename, "a") as f:
                note = input("Введите текст заметки: ")
                f.write(note + "\n")
            print("Заметка добавлена.")
        except FileNotFoundError:
            print("Файл не найден. Сначала создайте файл.")
        except Exception as e:
            print(f"Ошибка при добавлении заметки: {e}")

    elif choice == "view":
        try:
            with open(filename, "r") as f:
                lines = f.readlines()
                if not lines:
                    print("Файл пуст.")
                else:
                    for i, line in enumerate(lines):
                        print(f"{i + 1}. {line.strip()}")
        except FileNotFoundError:
            print("Файл не найден. Сначала создайте файл.")
        except Exception as e:
            print(f"Ошибка при просмотре заметок: {e}")

    elif choice == "exit":
        print("Программа завершена.")
        break
    else:
        print("Неизвестная команда. Попробуйте снова.")
