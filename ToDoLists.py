import os

def display_menu():
    print("\nOptions")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Remove Task")
    print("5. Quit")

def view_todo_list():
    try:
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("To-Do List is empty.")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task.strip()}")
    except FileNotFoundError:
        print("To-Do List is empty.")

def add_task():
    task = input("Enter the task: ")
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully.")

def mark_task_done():
    view_todo_list()
    try:
        task_index = int(input("Enter the task number to mark as done: ")) - 1
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
        if 0 <= task_index < len(tasks):
            tasks[task_index] = "[Done] " + tasks[task_index]
            with open("todo.txt", "w") as file:
                file.writelines(tasks)
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def remove_task():
    view_todo_list()
    try:
        task_index = int(input("Enter the task number to remove: ")) - 1
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            with open("todo.txt", "w") as file:
                file.writelines(tasks)
            print(f"Task removed: {removed_task.strip()}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_todo_list()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_task_done()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
