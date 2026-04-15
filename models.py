import uuid

# רשימת המשימות - זמני עד שנעבור ל-DB
# hardcoded לעכשיו כי אין עדיין DB
tasks = [
    {"id": "1", "title": "Learn Flask", "completed": False},
    {"id": "2", "title": "Build API", "completed": False},
    {"id": "3", "title": "Test with Postman", "completed": True}
]

def get_all_tasks():
    return tasks

# מחפש לפי id שמגיע מה-URL - string בגלל UUID
def get_task_by_id(id):
    for t in tasks:
        if t["id"] == id:
            return t
    # אם לא מצא - מחזיר None, ה-route מחליט מה לעשות
    return None

def create_task(task_data):
    # uuid4 כי צריך string serializable ל-JSON
    new_task = {
        "id": str(uuid.uuid4()),
        "title": task_data["title"],
        "completed": False  # תמיד מתחיל כ-False
    }
    tasks.append(new_task)
    return new_task

# עדכון - רק מה שנשלח, לא כופה כלום
def update_task(task_id, task_data):
    for task in tasks:
        if task["id"] == task_id:
            if "title" in task_data:
                task["title"] = task_data.get("title")
            if "completed" in task_data:
                task["completed"] = task_data["completed"]
            return task
    return None

def delete_task(task_id):
    for i, t in enumerate(tasks):
        if t["id"] == task_id:
            tasks.pop(i)
            return True
    return None