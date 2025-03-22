def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Найти индекс минимального элемента в неопределенной части массива
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Переместить найденный минимальный элемент в начало неопределенной части массива
        arr[i], arr[min_index] = arr[min_index], arr[i]


def main():
    while True:
        try:
            # Запрос ввода списка чисел
            user_input = input("Введите список чисел через пробел: ")
            number_list = list(map(int, user_input.split()))

            # 1. Находим максимальное значение
            max_value = max(number_list)
            print(f"Максимальное значение в списке: {max_value}")

            # 2. Сортируем список с использованием сортировки выбора
            selection_sort(number_list)
            print(f"Отсортированный список: {number_list}")

            # 3. Запрашиваем у пользователя число для поиска
            search_number = int(input("Введите число для поиска: "))
            count = 0

            # 4. Подсчитываем, сколько раз число встречается в списке
            for number in number_list:
                if number == search_number:
                    count += 1
            print(f"Число {search_number} встречается {count} раз(а) в списке.")
            break  # Выйдем из цикла, если всё прошло успешно
        except ValueError:
            print("Ошибка: пожалуйста, введите только целые числа через пробел.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()