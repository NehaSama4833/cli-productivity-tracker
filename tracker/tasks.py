from .storage import load_tasks, save_tasks



def add_task(title):
    tasks = load_tasks()

    new_id = len(tasks) + 1
    task = {
        "id": new_id,
        "title": title,
        "done": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print(f"Task added: {title}")

def list_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks found")
        return

    for task in tasks:
        status = "✓" if task["done"] else "✗"
        print(f'{task["id"]}. {task["title"]} [{status}]')

def mark_done(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print(f"Task {task_id} marked as done")
            return

    print("Task not found")

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]

    if len(tasks) == len(new_tasks):
        print("Task not found")
        return

    save_tasks(new_tasks)
    print(f"Task {task_id} deleted")


