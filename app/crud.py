from models import Task
from json_services import load_data, save_data
from utils import to_dict, next_id

FILENAME = "tasks.json"

def add_task(task: Task):
    data = load_data(FILENAME)
    new_task = to_dict(task)
    new_task["id"] = next_id(data)
    data.append(new_task)
    save_data(filename=FILENAME, data=data)

def get_all_tasks() -> list:
    data = load_data(FILENAME)
    return data

def get_task_by_id(task_id: int) -> dict | None:
    data = load_data(FILENAME)
    for task in data:
        if task["id"] == task_id:
            return task
    return None

def update_task(task_id: int, updated_task: Task) -> bool:
    data = load_data(FILENAME)
    for i, task in enumerate(data):
        if task["id"] == task_id:
            updated_task_dict = to_dict(updated_task)
            updated_task_dict["id"] = task_id  # Ensure the ID remains the same
            data[i] = updated_task_dict
            save_data(filename=FILENAME, data=data)
            return True
    return False

def delete_task(task_id: int) -> bool:
    data = load_data(FILENAME)
    for i, task in enumerate(data):
        if task["id"] == task_id:
            del data[i]
            save_data(filename=FILENAME, data=data)
            return True
    return False

def delete_all_tasks() -> None:
    save_data(filename=FILENAME, data=[])