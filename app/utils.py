from models import Task


def to_dict(task: Task) -> dict:
    """Cette focntion permet de convertir un objet de type 'Task' en dict"""
    return {
        "id": task.id,
        "description": task.description,
        "status": task.status,
        "createdAt": task.createdAt,
        "updatedAt": task.updateAt
    }

