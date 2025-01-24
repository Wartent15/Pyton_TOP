def main():
    tasks = []

    while True:
        command = input("Введите команду (add, remove, list, exit): ").strip().lower()

        if command == "add":
            task = input("Введите описание задачи: ").strip()
            if task:
                tasks.append(task)
                print(f"Задача '{task}' добавлена в список.")
            else:
                print("Ошибка: Невозможно добавить пустую задачу.")

        elif command == "remove":
            try:
                index = int(input("Введите индекс задачи для удаления: "))
                removed_task = tasks.pop(index)
                print(f"Задача '{removed_task}' была удалена из списка.")
            except IndexError:
                print("Ошибка: Задача с таким индексом не существует.")
            except ValueError:
                print("Ошибка: Пожалуйста, введите корректный числовой индекс.")

        elif command == "list":
            if tasks:
                print("Список задач:")
                for i, task in enumerate(tasks):
                    print(f"{i}: {task}")
            else:
                print("Список задач пуст.")

        elif command == "exit":
            print("Выход из программы.")
            break

        else:
            print("Ошибка: Неизвестная команда, попробуйте ещё раз.")

if __name__ == "__main__":
    main()