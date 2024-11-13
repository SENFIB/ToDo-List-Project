import os
import json
from datetime import datetime


# Func For Read ToDo List

def read_tasks():
    """The Function Can Read"""

    if not os.path.exists("ToDo List.json") or os.stat("ToDo List.json").st_size == 0:
        return []

    with open("ToDo List.json", "r") as r:
        return json.load(r)

# Func For Add Task To ToDo List
def edit_task():
    """The Function Can Edit With Any Input Of User And Add Task To List"""

    # This Loop Ask Of User
    while True:
        # The Empty Print For Better Interface
        print()
        # If User Select Any Options Can Use Easy Of This TODO List
        user_to_do = input("Enter Your The To Do list:\nFor Change Status Task Type Task:\n"
                           "For Deleted Type Delete:\nFor See Your List Type List:\nFor Quit Type Exit:\n")

        if user_to_do.casefold() == "exit":
            print("_" * 30)
            print("Thank You For Using My app!")
            print("^" * 30)
            exits_file()
            break


        elif user_to_do.casefold() == "list":
            # Use Func For Read Json File
            user_read = read_tasks()
            try:
                # Loop For Print Tasks
                for index, tasks in enumerate(user_read, 1):
                    completed = "❌" if not tasks["completed"] else "✔️"
                    print("-" * 20)
                    print("*" * 10, index, "*" * 10)
                    print(f"Title: {tasks["Title"]}")
                    print(f"Date: {tasks["Date"]}")
                    print(f"Status: {completed}")
                    print("_" * 20)
                # For Show Empty List
                if len(user_read) == 0:
                    print("Not in List")

            except ValueError:
                print("Invalid Input")

        elif user_to_do.casefold() == "task":
            try:
                change_task = int(input("Enter Your The To Do List Number:\n"))
                # Use Func For Read Json File
                json_read = read_tasks()
                # Find Number Of Task And Change Status
                if 0 < change_task <= len(json_read):
                    task = json_read[change_task - 1]
                    task["completed"] = not task ["completed"]
                    with open("ToDo List.json", "w") as nw:
                        json.dump(json_read, nw, indent=4)
                    print("Task status updated")

            except ValueError:
                print("Invalid Number We Can't Change Status")

        elif user_to_do.casefold() == "delete":
            try:
                delete_task = int(input("Enter Your The To Do List Number:\n"))
                # Use Func For Read Json File
                json_read = read_tasks()
                # Find Task And Delete
                if 0 < delete_task <= len(json_read):
                    delete_task = json_read.pop(delete_task - 1)
                    with open("ToDo List.json", "w") as nw:
                        json.dump(json_read, nw, indent=4)
                    print(f"Task{delete_task} deleted.")

            except ValueError:
                print("Invalid Number We Can't Delete Status")



        else:
            # Use Func For Read Json File
            json_read = read_tasks()
            # Style Write In Json File
            dic_todo = {
                "Title": user_to_do,
                "Date": datetime.now().strftime("%m/%d/%Y -> %H:%M:%S"),
                "completed": False
            }
            # Add New Task To Json
            json_read.append(dic_todo)
            with open("ToDo List.json", "w") as w:
                json.dump(json_read, w, indent=4)
            print(f"Task {user_to_do} added to the list.")




# Func For Create ToDo List First
def exits_file():
    """The Func Create Json File If Don't File Exist"""

    if not os.path.exists("ToDo List.json"):
        with open("ToDo List.json", "w") as w:
            json.dump([], w)

edit_task()
