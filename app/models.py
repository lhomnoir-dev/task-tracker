from datetime import datetime

class Status:
    TODO = 'todo'
    IN_POGRESS = 'in-progress'
    DONE = 'done'

class Task:
    def __init__(self, description: str, status: str = Status.TODO):
        self.id = 0
        self.description = description
        self.status = status
        self.createdAt = datetime.utcnow()
        self.updateAt = datetime.utcnow()