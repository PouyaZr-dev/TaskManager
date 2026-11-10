import json
import os

DATA_DIR="data"
DATA_FILE = os.path.join(DATA_DIR,"tasks.json")

# بارگذاری وظایف از فایل JSON
def load_tasks():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(DATA_FILE):
        return[]
    try:
        with open(DATA_FILE,"r",encoding="utf-8")as f:
            return json.load(f)
    except json.JSONDecodeError:
        return[]

# ذخیره وظایف در فایل JSON
def save_tasks(tasks):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

# اضافه کردن وظیفه جدید
def add_task(title):
    tasks = load_tasks()
    task_id = tasks[-1]["id"] + 1 if tasks else 1
    new_task = {
        "id": task_id,
        "title": title,
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return "Task added successfully."

# حذف وظیفه بر اساس شناسه
def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [t for t in tasks if t["id"] != task_id]
    if len(updated_tasks) == len(tasks):
        return False, "Task ID not found."
    save_tasks(updated_tasks)
    return True, "Task deleted successfully."


# تغییر وضعیت انجام شده/نشده
def toggle_task_status(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            save_tasks(tasks)
            return True, "Task status updated."
    return False, "Task ID not found."