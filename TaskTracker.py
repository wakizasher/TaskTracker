'''
Task tracker is a project used to track and manage your tasks.
The application should run from the command line, accept user actions and inputs as arguments,
and store the tasks in a JSON file. The user should be able to:
- Add, Update, and Delete tasks
- Mark a task as in progress or done
- List all tasks
- List all tasks that are done
- List all tasks that are not done
- List all tasks that are in progress
'''
import json
from datetime import datetime


#TASK_ID = 0
#task_list = []
file = "task.json"
NOW = datetime.now().strftime("%d/%m/%Y")


try:
    with open(file, 'r') as read_file:
        loaded_tasks = json.load(read_file) # Use json.load() to read the data from the file
        task_list = loaded_tasks
        if task_list: #Check if the loaded list is not empty
            TASK_ID = max(task['id'] for task in task_list) # Find the maximum ID in the loaded tasks and set TASK_ID
        else:
            TASK_ID = 0 # If the file was empty or contained an empty string
except FileNotFoundError:
    # If the file doesn't exist, start with an empty list and TASK_ID = 0
    TASK_ID = 0
    task_list = []
    print(f"{file} not found. Starting with an empty task list.")
except json.JSONDecodeError:
    # Handle cases where the file exists but isn't valid JSON
    print(f"Error decoding JSON from {file}")
    TASK_ID = 0
    task_list = []


def add(task: str, status: str) -> dict:
    global TASK_ID
    global NOW
    TASK_ID += 1
    new_dictionary = {
        'id': TASK_ID,
        'task': task,
        'status': status,
        'createdAt': NOW,
        'updatedAt': NOW
    }
    task_list.append(new_dictionary)
    return new_dictionary


def update(id:int, **kwargs) -> bool:
    global NOW
    for i, task in enumerate(task_list):
        if task['id'] == id: # Update the updatedAt field
           for key, value in kwargs.items():
               if key in task:
                   task_list[i][key] = value # Update the task in the list
           task_list[i]['updatedAt'] = NOW # Update the 'updatedAt' field
           with open(file,"w") as write_file:
               json.dump(task_list, write_file, indent=4)
               print(f"Task with ID {id} has been updated {NOW}.")
           return True
    print(f"No task has been updated.")
    return False


def delete(delete_id):
    with open(file,"r") as read_file:
        data = json.load(read_file)
        for row in data:
            if row['id'] == delete_id:
                removed_value = data[delete_id]

                del data[delete_id]

    with open(file,"w") as f:
        json.dump(data,f,indent=4)


print("Welcome to TaskTracker")
print("======================")
print("Press 1 to display the tasks")
print("Press 2 to add the task")
print("Press 3 to update the task")
print("Press 4 to delete the task")
print("======================")
menu = int(input("Enter the option number: "))

if menu == 1:
    with open(file, 'r') as file_to_display:
        tasks = json.load(file_to_display)
    print("All current tasks: ")
    print(tasks)
elif menu == 2:
    while True:
        task = input("Please enter your task: ")
        if task.lower() == 'quit':
            break
        status = input("Please enter your status (todo, in-progress, done): ")
        add(task, status)
        print("Task added successfully (ID: 1)")

    with open(file, "w") as write_file:
        json.dump(task_list, write_file, indent=4)
elif menu == 3:
    while True:
        id_update = int(input("Please enter task ID that you want to update (press 0 to quit): "))
        if id_update == 0:
            break
        task_update = input("Enter new task description (or press enter to skip): ")
        status_update = input("Enter new status for the task (or press enter to skip): ")
        kwargs = {}
        if task_update:
            kwargs['task'] = task_update
        if status_update:
            kwargs['status'] = status_update
        if update(id_update, **kwargs):
            print("Task with {id} updated successfully")
        else:
            print("Invalid task ID. Please enter a number ")











