import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from the text file if it exists."""
    if not os.path.exists(TASKS_FILE):
        return []

    with open(TASKS_FILE, "r") as file:
        tasks = file.read().splitlines()
    return tasks


def save_tasks(tasks):
    """Save the list of tasks to the text file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def add_task(tasks):
    """Ask the user to type a new task and add it."""
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {task}")


def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks found.")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()


def main():
    tasks = load_tasks()

    while True:
        print("=== Daily Task Tracker ===")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
