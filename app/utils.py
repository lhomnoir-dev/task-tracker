from models import Task
from datetime import datetime

def to_dict(task: Task) -> dict:
    """Cette focntion permet de convertir un objet de type 'Task' en dict"""
    created_at = task.createdAt.isoformat() if isinstance(task.createdAt, datetime) else task.createdAt
    updated_at = task.updateAt.isoformat() if isinstance(task.updateAt, datetime) else task.updateAt
    return {
        "id": task.id,
        "description": task.description,
        "status": task.status,
        "createdAt": created_at,
        "updatedAt": updated_at
    }

def from_dict(data: dict) -> Task:
    """Cette fonction permet de convertir un dict en objet de type 'Task'"""
    task = Task(description=data["description"], status=data["status"])
    task.id = data["id"]
    task.createdAt = datetime.fromisoformat(data["createdAt"]) if isinstance(data["createdAt"], str) else data["createdAt"]
    task.updateAt = datetime.fromisoformat(data["updatedAt"]) if isinstance(data["updatedAt"], str) else data["updatedAt"]
    return task

def next_id(tasks: list) -> int:
    """Cette fonction permet de générer un identifiant unique pour une nouvelle tâche"""
    if not tasks:
        return 1
    else:
        return max(task["id"] for task in tasks) + 1