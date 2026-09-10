from models import Task
from json_services import load_data, save_data
from utils import to_dict

FILENAME = "tasks.json"

def add_task(task: Task):
    data = load_data(FILENAME)
    new_task = to_dict(task)
    data.append(new_task)
    save_data(filename=FILENAME, data=data)