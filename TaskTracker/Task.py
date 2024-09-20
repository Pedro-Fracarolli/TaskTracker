import datetime

class Task:
    id : int
    description : str
    status : str
    createdAt: datetime

    def __init__(self, description, status):
        self.description = description
        self.status = status
        self.createdAt = datetime.datetime.now().strftime("%d/%m/%Y - %X")

    def __str__(self):
        return f"Task: {self.description} - Status: {self.status} - created At: {self.createdAt}"

