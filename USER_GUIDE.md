# Todo Application - User Guide

## Overview
The Todo application is a command-line interface (CLI) application that allows you to manage your tasks. It stores all tasks in memory only, which means tasks are not saved when you close the application.

## How to Run the Application
Open your terminal/command prompt and run:
```
python -m src.cli.todo_app
```

## Main Menu
When you run the application, you'll see the main menu:
```
=== Todo App ===
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Toggle Completion
6. Exit
===============
```

## Features Explained

### 1. Add Task
- Select option `1`
- Enter your task title when prompted
- The application will assign a unique ID to your task
- Example:
  ```
  Choose an option (1-6): 1
  Enter task title: Buy groceries
  Task added with ID: 1
  ```

### 2. View Tasks
- Select option `2`
- See all your tasks with their ID, title, and completion status
- Example:
  ```
  Choose an option (1-6): 2

  Your Tasks:
  ID: 1 | Title: Buy groceries | Status: Pending
  ID: 2 | Title: Walk the dog | Status: Pending
  ```

### 3. Update Task
- Select option `3`
- Enter the task ID you want to update
- Enter the new title for the task
- Example:
  ```
  Choose an option (1-6): 3
  Enter task ID to update: 1
  Enter new title: Buy weekly groceries
  Task 1 updated successfully!
  ```

### 4. Delete Task
- Select option `4`
- Enter the task ID you want to delete
- The task will be permanently removed
- Example:
  ```
  Choose an option (1-6): 4
  Enter task ID to delete: 2
  Task 2 deleted successfully!
  ```

### 5. Toggle Completion
- Select option `5`
- Enter the task ID you want to mark as complete/incomplete
- The completion status will flip from pending to complete or vice versa
- Example:
  ```
  Choose an option (1-6): 5
  Enter task ID to toggle completion: 1
  Task 1 is now completed!
  ```

### 6. Exit
- Select option `6`
- Safely close the application
- Example:
  ```
  Choose an option (1-6): 6
  Goodbye!
  ```

## Example Session
Here's how a typical session might look:
```
Welcome to the Todo App!

=== Todo App ===
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Toggle Completion
6. Exit
===============
Choose an option (1-6): 1
Enter task title: Buy milk
Task added with ID: 1

Choose an option (1-6): 1
Enter task title: Call mom
Task added with ID: 2

Choose an option (1-6): 2

Your Tasks:
ID: 1 | Title: Buy milk | Status: Pending
ID: 2 | Title: Call mom | Status: Pending

Choose an option (1-6): 5
Enter task ID to toggle completion: 1
Task 1 is now completed!

Choose an option (1-6): 2

Your Tasks:
ID: 1 | Title: Buy milk | Status: Completed
ID: 2 | Title: Call mom | Status: Pending

Choose an option (1-6): 6
Goodbye!
```

## Important Notes
- All data is stored in memory only (not saved to disk)
- Tasks are lost when the application closes
- The application handles invalid inputs gracefully
- Task IDs are automatically assigned and cannot be changed
- Empty task titles are not allowed