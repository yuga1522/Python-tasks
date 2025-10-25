import os
from datetime import datetime

# Step 1: Define the file name to store tasks persistently
TASK_FILE = "todo_tasks.txt"

# Step 2: Load tasks from the file and parse into structured data
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    tasks = []
    with open(TASK_FILE, "r") as file:
        for line in file:
            parts = line.strip().split(" | ")
            if len(parts) == 4:
                created, task, due, status = parts
                tasks.append({
                    "created": created.replace("Created: ", ""),
                    "task": task.replace("Task: ", ""),
                    "due": due.replace("Due: ", ""),
                    "completed": status.replace("Completed: ", "") == "True"
                })
    return tasks

# Step 3: Save structured tasks back to the file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for t in tasks:
            line = f"Created: {t['created']} | Task: {t['task']} | Due: {t['due']} | Completed: {t['completed']}"
            file.write(line + "\n")

# Step 4: Add a new task with due date and time
def add_task():
    task = input("Enter your task (special characters allowed): ").strip()
    if not task:
        print("❌ Task cannot be empty.\n")
        return

    due_date = input("Enter due date (YYYY-MM-DD): ").strip()
    due_time = input("Enter due time (HH:MM): ").strip()

    try:
        due_datetime = datetime.strptime(f"{due_date} {due_time}", "%Y-%m-%d %H:%M")
    except ValueError:
        print("❌ Invalid date or time format.\n")
        return

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M")
    tasks = load_tasks()
    tasks.append({
        "created": created_at,
        "task": task,
        "due": due_datetime.strftime("%Y-%m-%d %H:%M"),
        "completed": False
    })
    save_tasks(tasks)
    print("✅ Task added successfully!\n")

# Step 5: View all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.\n")
        return
    print("\n🗂️ Your To-Do List:")
    for i, t in enumerate(tasks):
        status = "✅ Done" if t["completed"] else "❌ Pending"
        print(f"{i+1}. {t['task']} | Due: {t['due']} | {status}")
    print()

# Step 6: Remove a task
def remove_task():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks to remove.\n")
        return
    view_tasks()
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if index < 0 or index >= len(tasks):
            print("❌ Invalid task number.\n")
            return
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"✅ Removed: {removed['task']}\n")
    except ValueError:
        print("❌ Invalid input. Please enter a number.\n")

# Step 7: Mark a task as completed
def mark_task_completed():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks to mark.\n")
        return
    view_tasks()
    try:
        index = int(input("Enter task number to mark as completed: ")) - 1
        if index < 0 or index >= len(tasks):
            print("❌ Invalid task number.\n")
            return
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print(f"✅ Task marked as completed: {tasks[index]['task']}\n")
    except ValueError:
        print("❌ Invalid input.\n")

# Step 8: Alert for tasks due today or overdue
def due_task_alert():
    tasks = load_tasks()
    now = datetime.now()
    due_today = []
    overdue = []

    for t in tasks:
        try:
            due_dt = datetime.strptime(t["due"], "%Y-%m-%d %H:%M")
            if not t["completed"]:
                if due_dt.date() == now.date():
                    due_today.append(t)
                elif due_dt < now:
                    overdue.append(t)
        except ValueError:
            continue

    if due_today:
        print("\n📅 Tasks Due Today:")
        for t in due_today:
            print(f"- {t['task']} | Due: {t['due']}")
    if overdue:
        print("\n⏰ Overdue Tasks:")
        for t in overdue:
            print(f"- {t['task']} | Due: {t['due']}")
    if not due_today and not overdue:
        print("\n✅ No tasks due today or overdue.\n")
    else:
        print()

# Step 9: Main menu loop
def main():
    while True:
        print("===== Personal To-Do Reminder App =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Due Task Alert")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            mark_task_completed()
        elif choice == '5':
            due_task_alert()
        elif choice == '6':
            print("👋 Exiting To-Do App. Stay productive!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

# Step 10: Run the program
if __name__ == "__main__":
    main()
