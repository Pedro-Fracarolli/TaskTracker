from Task import Task

tasks_list = []

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

    def ListTasks(self):

        print("List: ")
        print("1. All tasks")
        print("2. Todo tasks")
        print("3. In-Progress tasks")
        print("4. Done tasks")
        decision = int(input("- "))

        match(decision):
            case 1:
                for index, tasks in enumerate(tasks_list):
                    print(index + 1, ". ", tasks)
            case 2:
                for index, task in enumerate(tasks_list):
                    if task.status == "Todo":
                        print(index + 1, ". ", task)
            case 3:
                for index, task in enumerate(tasks_list):
                    if task.status == "In-Progress":
                        print(index + 1, ". ", task)
            case 4:
                for index, task in enumerate(tasks_list):
                    if task.status == "Done":
                        print(index + 1, ". ", task)

        print("----------------------------------------------------")
        option = input("do you want to update/delete a task? Y/N - ").lower()

        if option == "y":
            index = int(input("Task Id: "))
            task = tasks_list[index]
            print(task)
            print("Do you want to:")
            print("1. Update")
            print("2. Delete")
            decision = int(input("- "))
            if decision == 1:
                self.UpdateTask(task)
            elif decision == 2:
                self.DeleteTask(task)
        elif option == "n":
            print("Returning...")

    def UpdateTask(self, task):
        print("Update task:")
        print("1. Description")
        print("2. Status")
        choice = int(input("- "))

        if choice == 1:
            new_description = input("New description: ")
            print("Old description: " + task.description)
            task.description = new_description
            print("New description: " + task.description)
        elif choice == 2:
            print("New status: ")
            print("1. Todo")
            print("2. In-Progress")
            print("3. Done")
            new_status = int(input("- "))

            print("Old status: " + task.status)
            match(new_status):
                case 1:
                    task.status = "Todo"
                case 2:
                    task.status = "In-Progress"
                case 3:
                    task.status = "Done"
                case _:
                    print("Invalid input!")
            print("New status: " + task.status)



    def DeleteTask(self, task):
        choice = input("Are you sure you want to delete this task? Y/N - ").lower()

        if choice == "y":
            try:
                tasks_list.remove(task)
            except:
                print("An error occurred!")
            else:
                print("Task removed successfully!")
        elif choice == "n":
            print("Returning...")
