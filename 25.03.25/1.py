import json
import os

# Класс Task
class Task:
    def __init__(self, title, is_done=False):
        self.title = title
        self.is_done = is_done

    def mark_done(self):
        """Помечает задачу как выполненную."""
        self.is_done = True

    def to_dict(self):
        """Преобразует объект в словарь для сохранения в JSON."""
        return {"title": self.title, "is_done": self.is_done}

    @classmethod
    def from_dict(cls, data):
        """Создает объект Task из словаря."""
        return cls(data["title"], data["is_done"])


# Класс TaskManager
class TaskManager:
    FILE_NAME = "tasks.json"

    def __init__(self):
        self.tasks = []
        self.load_from_file()

    def add_task(self, title):
        """Добавляет новую задачу."""
        self.tasks.append(Task(title))
        print(f'Задача "{title}" добавлена.')

    def mark_task_done(self, title):
        """Отмечает задачу как выполненную."""
        for task in self.tasks:
            if task.title == title:
                task.mark_done()
                print(f'Задача "{title}" отмечена как выполненная.')
                return
        print(f'Задача "{title}" не найдена.')

    def show_tasks(self):
        """Выводит список задач."""
        if not self.tasks:
            print("Список задач пуст.")
        else:
            for idx, task in enumerate(self.tasks, 1):
                status = "Выполнено" if task.is_done else "Не выполнено"
                print(f"{idx}. {task.title} - {status}")

    def save_to_file(self):
        """Сохраняет задачи в файл."""
        with open(self.FILE_NAME, "w", encoding="utf-8") as file:
            json.dump([task.to_dict() for task in self.tasks], file, ensure_ascii=False, indent=4)

    def load_from_file(self):
        """Загружает задачи из файла."""
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "r", encoding="utf-8") as file:
                try:
                    data = json.load(file)
                    self.tasks = [Task.from_dict(task) for task in data]
                except json.JSONDecodeError:
                    self.tasks = []


# Функция для работы с пользователем
def main():
    manager = TaskManager()

    while True:
        command = input("Введите команду (add, done, show, exit): ").strip().lower()

        if command == "add":
            title = input("Введите название задачи: ").strip()
            if title:
                manager.add_task(title)
            else:
                print("Название задачи не может быть пустым.")

        elif command == "done":
            title = input("Введите название задачи: ").strip()
            manager.mark_task_done(title)

        elif command == "show":
            manager.show_tasks()

        elif command == "exit":
            manager.save_to_file()
            print("Данные сохранены. Программа завершена.")
            break

        else:
            print("Неизвестная команда. Используйте: add, done, show, exit.")

# Запуск программы
if __name__ == "__main__":
    main()