# Task Tracker

A simple command-line task management application that helps you track and organize your tasks efficiently. The project idea retrieved from https://roadmap.sh/projects/task-tracker

## Overview

Task Tracker is a Python-based command-line application that allows you to manage your tasks through a simple interface. The application stores all tasks in a JSON file, making it easy to maintain task persistence between sessions.

## Features

- **Add new tasks** with custom descriptions and status
- **Update existing tasks** including their description and status
- **Delete tasks** you no longer need
- **View all tasks** in your task list
- **Filter tasks by status:**
  - Show only completed tasks
  - Show only pending tasks
  - Show only in-progress tasks

## Installation

1. Clone this repository or download the source code
2. Make sure you have Python 3.x installed
3. No additional libraries are required as the application uses only standard library modules

## Usage

Run the application from your command line:

`python task_tracker.py`

### Menu Options

The application presents a menu with the following options:

1. **Display all tasks** - View all your current tasks
2. **Add a task** - Create a new task with description and status
3. **Update a task** - Modify the description or status of an existing task
4. **Delete a task** - Remove a task by its ID
5. **Show tasks that are not done** - Filter to see only pending tasks
6. **Show tasks that are in progress** - Filter to see only tasks marked as in-progress
7. **Show tasks that are done** - Filter to see only completed tasks

### Task Statuses

Tasks can have one of these statuses:
- `todo` - Tasks that are pending
- `in-progress` - Tasks that are currently being worked on
- `done` - Tasks that have been completed

### Data Storage

All tasks are stored in a `task.json` file in the same directory as the script. The file will be created automatically when you add your first task.

## Task JSON Structure

Each task is stored with the following information:
    
    {
        "id": 1,
        "task": "Task description",
        "status": "todo",
        "createdAt": "20/05/2025",
        "updatedAt": "20/05/2025"
    }

## Examples 

### Adding a Task
```
Enter the option number: 2 \n
Please enter your task: Complete the project documentation 
Please enter your status (todo, in-progress, done): todo
Please enter your task: quit
```
### Updating a Task 
```
Enter the option number: 3
Please enter task ID that you want to update (press 0 to quit): 1
Enter new task description (or press enter to skip): 
Enter new status for the task (or press enter to skip): in-progress
Please enter task ID that you want to update (press 0 to quit): 0
```
### Viewing Tasks

Enter the option number: 1
All current tasks:

    {
        "id": 1,
        "task": "Complete the project documentation",
        "status": "in-progress",
        "createdAt": "20/05/2025",
        "updatedAt": "20/05/2025"
    }

## Contributing 

Contributions, improvements, and bug fixes are welcome. Feel free to fork this repository and submit pull requests.

## License 

This project is open source and available under the MIT License.
