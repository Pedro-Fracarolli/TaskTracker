from TaskManager import TaskManager

"""
Task tracker is a project used to track and manage your tasks.
In this task, you will build a simple command line interface (CLI)
to track what you need to do, what you have done, and what you are currently working on.
This project will help you practice your programming skills, including:
working with the filesystem, handling user inputs, and building a simple CLI application.
"""
class Menu():

    while(True):
        print("-----TASKTRACKER-----")
        print("1. Add task")
        print("2. List tasks")
        print("3. Save Tasks")
        print("4. Import Tasks")
        option = int(input("- "))

        task_manager = TaskManager()
        match(option):
            case 1:
                task_manager.AddTask()
            case 2:
                task_manager.ListTasks()
            case 3:
                task_manager.SaveTasks()
            case 4:
                task_manager.ImportTasks()


