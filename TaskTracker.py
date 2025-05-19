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
import os

#TASK_ID = 0
#task_list = []
file = "task.json"
NOW = datetime.now().strftime("%d/%m/%Y")
path = f"./{file}"
check_file = os.path.isfile(path)


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
    with open(file, "w") as write_file:
        json.dump(task_list, write_file, indent=4)
    return True


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


def delete(delete_id: int):
    updated_data = []

    try:
        with open(file, 'r') as read_file:
            loaded_list_of_tasks = json.load(read_file)

    except (FileNotFoundError, json.JSONDecodeError):
        print("Ошибка чтения файла")
        return False
    list_of_tasks = loaded_list_of_tasks
    initial_task_count = len(loaded_list_of_tasks)
    for i, task in enumerate(list_of_tasks):
        if task['id'] != delete_id:
            updated_data.append(task)

    final_task_count = len(updated_data)

    if final_task_count < initial_task_count:
        task_found_and_deleted = True
    else:
        task_found_and_deleted = False
    if task_found_and_deleted or initial_task_count == 0:
        with open(file, 'w') as write_file:
            json.dump(updated_data,write_file,indent=4)
    if task_found_and_deleted:
        print(f"Таск с ID {delete_id} успешно удален.")
        return True
    else:
        print(f"Таск с ID {delete_id} не найден.")
        return False



def list_tasks_that_are_done():
    try:
        with open(file, 'r') as read_file:
            loaded_list_of_tasks = json.load(read_file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("File not found")
        return
    # Check tasks that are Not 'done'
    all_tasks_are_done = True # Assume that everything is done
    tasks_are_available = False # Flag to check if there are any tasks

    if loaded_list_of_tasks:
        tasks_are_available = True
        for task in loaded_list_of_tasks:
            status = task.get('status')
            if status is not None and status != 'done':
                all_tasks_are_done = False # Found task not in 'done' status
    else:
        tasks_are_available = False # The list is empty
    found_done_tasks = False
    if loaded_list_of_tasks:
        for i, task in enumerate(loaded_list_of_tasks):
            if task['status'] == 'done':
                print("\n---Tasks that has 'done' status: ---")
                print(json.dumps(task,indent=4))
    if not found_done_tasks and tasks_are_available:
        print("No current 'done' tasks")


def list_tasks_that_are_not_done():
    try:
        with open(file, 'r') as read_file:
            loaded_list_of_tasks = json.load(read_file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("File does not exists")
        return
    all_tasks_are_not_done = True  # Assume that everything is not done
    tasks_are_available = False  # Flag to check if there are any tasks
    if loaded_list_of_tasks:
        tasks_are_available = True
        for task in loaded_list_of_tasks:
            status = task.get('status')
            if status is not None and status == 'done':
                all_tasks_are_not_done = False
    else:
        tasks_are_available = False # The list is empty
    found_not_done_tasks = False
    if loaded_list_of_tasks:
        for i, task in enumerate(loaded_list_of_tasks):
            if task['status'] != 'done':
                print("\n---Tasks that has 'done' status: ---")
                print(json.dumps(task,indent=4))
    if not found_not_done_tasks and tasks_are_available:
        print("No current undone tasks")


def list_tasks_that_are_inprogress():
    try:
        with open(file, 'r') as read_file:
            loaded_list_of_tasks = json.load(read_file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("File not found")
        return
    all_tasks_are_inprogress = True  # Assume that everything is not done
    tasks_are_available = False  # Flag to check if there are any tasks
    if loaded_list_of_tasks:
        tasks_are_available = True
        for task in loaded_list_of_tasks:
            status = task.get('status')
            if status is not None and status == 'in-progress':
                all_tasks_are_not_done = False
    else:
        tasks_are_available = False # The list is empty
    found_not_done_tasks = False
    if loaded_list_of_tasks:
        for i, task in enumerate(loaded_list_of_tasks):
            if task['status'] == 'in-progress':
                print("\n---Tasks that has 'in-progress' status: ---")
                print(json.dumps(task,indent=4))


def display_menu():
    print("\n========== TaskTracker Menu ==========")
    print("======================")
    print("Press 1 to display the tasks")
    print("Press 2 to add the task")
    print("Press 3 to update the task")
    print("Press 4 to delete the task")
    print("Press 5 to show tasks that are not done")
    print("Press 6 to show tasks that are in progress")
    print("Press 7 to show tasks that are done")
    print("======================")


display_menu()
menu = int(input("Enter the option number: "))

if menu == 1:
    if check_file == True:
        with open(file, 'r') as file_to_display:
            all_tasks = json.load(file_to_display)
        print("All current tasks: ")
        print(json.dumps(all_tasks,indent=4))
    else:
        print("File does not exists, add tasks")


elif menu == 2:
    while True:
        enter_task = input("Please enter your task: ")
        if enter_task.lower() == 'quit':
            break
        status = input("Please enter your status (todo, in-progress, done): ")
        add(enter_task, status)
        print(f"Task added successfully (ID: {TASK_ID})")


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


elif menu == 4:
    while True:
        delete_task = int(input("Please enter task ID you wont to delete, to quit hit \'0\': "))
        if delete_task == 0:
            break
        delete(delete_task)


elif menu == 5:
    list_tasks_that_are_not_done()


elif menu == 6:
    list_tasks_that_are_inprogress()


elif menu == 7:
    list_tasks_that_are_done()










