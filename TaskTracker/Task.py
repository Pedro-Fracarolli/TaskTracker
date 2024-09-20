import datetime

class Task:
    id: int
    description: str
    status: str
    createdAt: str  # This should be a string, since you are formatting it as a string in __init__

    def __init__(self, description, status, createdAt=None):
        self.description = description
        self.status = status
        # If createdAt is provided (during import), use it; otherwise, use the current date/time
        self.createdAt = createdAt if createdAt else datetime.datetime.now().strftime("%d/%m/%Y - %X")

    def __str__(self):
        return f"Task: {self.description} - Status: {self.status} - created At: {self.createdAt}"


    def to_dict(self):
        return {
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt  # No space in key name
        }


