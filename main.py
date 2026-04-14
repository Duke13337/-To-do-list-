tasks = []
print("Программа запущена")


def main():
    tasks = []  # Список для хранения задач

    while True:
        print("\n--- Список задач ---")
        print("1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Выйти")
        
        choice = input("Выберите действие (1-4): ")

        if choice == '1':
            if not tasks:
                print("Список пуст.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
        
        elif choice == '2':
            new_task = input("Введите задачу: ")
            tasks.append(new_task)
            print("Задача добавлена!")
            
        elif choice == '3':
            if not tasks:
                print("Нечего удалять.")
                continue
            num = int(input("Введите номер задачи для удаления: "))
            if 0 < num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Задача '{removed}' удалена.")
            else:
                print("Неверный номер.")
                
        elif choice == '4':
            print("Программа завершена.")
            break
        else:
            print("Ошибка: выберите пункт от 1 до 4.")

if __name__ == "__main__":
    main()
