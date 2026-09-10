from json_services import load_data, save_data
from models import Task
from crud import add_task

if __name__=="__main__":

    new_data = Task(description="strings")
    add_task(new_data)
    print(load_data("tasks.json"))
