tasks = []

def show_tasks():
    print("\nВаш список задач:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def add_task():
    name = input("Введите название задачи: ")
    tasks.append(name)
    print("Задача добавлена!")

def delete_task():
    show_tasks()
    if tasks:
        num = int(input("Введите номер задачи для удаления: "))
        removed = tasks.pop(num - 1)
        print(f"Задача '{removed}' удалена!")

if __name__ == "__main__":
    while True:
        print("\n1. Показать | 2. Добавить | 3. Удалить | 4. Выход")
        choice = input("Выбор: ")
        if choice == '1': show_tasks()
        elif choice == '2': add_task()
        elif choice == '3': delete_task()
        elif choice == '4': break
