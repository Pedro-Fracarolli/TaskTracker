# TaskTracker

## Overview

**TaskTracker** is a Python-based command-line application designed to help users manage their tasks efficiently. It allows users to create tasks, list them based on their current status, and update or delete them as needed. This project is a great way to practice working with the filesystem, handling user input, and building a simple CLI application.

The project consists of three main components:
- `tasktracker.py`: The main entry point for the TaskTracker application.
- `taskmanager.py`: Handles the core logic of adding, listing, updating, and deleting tasks.
- `task.py`: Defines the `Task` class, representing a task with its attributes such as description, status, and creation time.

## Features

- **Add Task**: Users can add a task with a description and status (Todo, In-Progress, Done).
- **List Tasks**: Displays tasks based on their status (All, Todo, In-Progress, Done).
- **Update Task**: Users can update the description or status of an existing task.
- **Delete Task**: Allows users to remove a task from the list.

## Files and Structure

### `tasktracker.py`

The `tasktracker.py` file acts as the main interface, where the user interacts with the application through a command-line menu. It provides options to add tasks and list them.

```python
class Menu():
    while(True):
        print("-----TASKTRACKER-----")
        print("1. Add task")
        print("2. List tasks")
        option = int(input("- "))

        task_manager = TaskManager()
        match(option):
            case 1:
                task_manager.AddTask()
            case 2:
                task_manager.ListTasks()
```
### `taskmanager.py`

The `taskmanager.py` class manages the list of tasks and provides methods for adding, listing, updating and deleting tasks.

```python
class TaskManager:
    def AddTask(self):
        global status
        description = input("Description: ")
        print("Status: ")
        print("1. Todo")
        print("2. In-Progress")
        print("3. Done")
        
        option = int(input("- "))
        
        match(option):
            case 1:
                status = "Todo"
            case 2:
                status = "In-Progress"
            case 3:
                status = "Done"

        new_task = Task(description, status)
        print("Task added successfully!")
        print(new_task)
        tasks_list.append(new_task)
    # More methods...
```

### `task.py`

The `task.py` file defines the `Task` class, which represents a task with a description, status, and the creation date.

```python
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
```
## How to Run
1. Clone the repository or download the project files.
2. Open a terminal and navigate to the project directory.
3. Run the `tasktracker.py` file:
```bash
python tasktracker.py
```
4. Follow the on-screen instructions to add, list, update or delete tasks.

## Requirements
- Python 3.x

## License and knowledgments
- This project is licensed under the MIT License.
- This project is a solution from the Backend Roadpmap: https://roadmap.sh/projects/task-tracker
