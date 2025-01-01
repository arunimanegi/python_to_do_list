import os

# To-Do List Application (Command-Line)

tasks = []

def show_menu():
    print("\n--- To-Do List Application ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks to display. Add some!")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, start=1):
            status = "[Done]" if task['done'] else "[Pending]"
            print(f"{idx}. {status} {task['title']}")

def add_task():
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    print(f"Task '{title}' added successfully!")

def mark_task_done():
    view_tasks()
    try:
        task_number = int(input("Enter task number to mark as done: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]['done'] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_number = int(input("Enter task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task['title']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main Application Loop
while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_task_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select again.")
