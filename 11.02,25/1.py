# user_manager_program.py

def add_user(users, name, age):
    if name in users:
        raise ValueError("Пользователь с таким именем уже существует.")
    if age < 0:
        raise ValueError("Возраст не может быть отрицательным.")
    users[name] = age
    print(f"Пользователь '{name}' добавлен.")


def remove_user(users, name):
    if name not in users:
        raise ValueError("Пользователь не найден.")
    del users[name]
    print(f"Пользователь '{name}' удален.")


def list_users(users):
    if not users:
        print("Нет пользователей.")
        return
    print("Список пользователей:")
    for name, age in users.items():
        print(f"Имя: {name}, Возраст: {age}")


def main():
    users = {}

    while True:
        command = input("Введите команду (add, remove, list, exit): ").strip().lower()

        if command == "add":
            name = input("Введите имя пользователя: ").strip()
            try:
                age = int(input("Введите возраст пользователя: "))
                add_user(users, name, age)
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif command == "remove":
            name = input("Введите имя пользователя для удаления: ").strip()
            try:
                remove_user(users, name)
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif command == "list":
            list_users(users)

        elif command == "exit":
            print("Выход из программы.")
            break

        else:
            print("Некорректная команда. Пожалуйста, введите add, remove, list или exit.")


if __name__ == "__main__":
    main()