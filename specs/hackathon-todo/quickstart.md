# Quickstart Guide: Hackathon Todo Project

**Date**: 2026-01-17
**Phase**: Phase I - In-Memory Python Console App
**Related**: specs/hackathon-todo/spec.md

## Overview

This guide provides instructions for getting started with the Hackathon Todo Project, beginning with Phase I implementation.

## Prerequisites

- Python 3.13+ installed on your system
- Basic command-line familiarity
- Understanding of the project goals and specifications

## Phase I Setup

### 1. Clone or Create Project Directory

Create a directory for your project:

```bash
mkdir hackathon-todo
cd hackathon-todo
```

### 2. Create Project Structure

Based on the planned architecture, create the following directory structure:

```bash
mkdir -p src/models src/store src/services src/cli
```

### 3. Install Dependencies (None Required for Phase I)

Phase I uses only standard Python libraries, so no external dependencies need to be installed.

## Phase I Usage

Once implemented, the CLI application will support the following operations:

### Running the Application

```bash
python src/cli/todo_app.py
```

### Available Operations

After launching, the application will present a menu with the following options:

1. **Add Task** - Create a new todo item
   - Prompts for task title
   - Automatically assigns a unique ID
   - Sets completion status to false

2. **View Tasks** - Display all current tasks
   - Shows ID, title, and completion status for each task
   - Lists all tasks in the in-memory store

3. **Update Task** - Modify an existing task's title
   - Prompts for task ID
   - Prompts for new title
   - Validates that the task exists

4. **Delete Task** - Remove a task from the list
   - Prompts for task ID
   - Removes the task from memory
   - Validates that the task exists

5. **Toggle Completion** - Mark a task as complete/incomplete
   - Prompts for task ID
   - Flips the completion status
   - Validates that the task exists

6. **Exit** - Close the application

### Example Workflow

```
Welcome to the Todo App!

Choose an option:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Toggle Completion
6. Exit

> 1
Enter task title: Buy groceries
Task added with ID: 1

> 2
Tasks:
ID: 1 | Title: Buy groceries | Completed: False

> 5
Enter task ID to toggle: 1
Task 1 completion status toggled

> 2
Tasks:
ID: 1 | Title: Buy groceries | Completed: True

> 6
Goodbye!
```

## Phase II Preparation

When the project evolves to Phase II, additional setup will be required:

- Database setup (Neon Serverless PostgreSQL)
- Authentication system (Better Auth)
- Web framework (Next.js, FastAPI)
- API endpoint configuration

## Troubleshooting

### Common Issues

**Application crashes on startup:**
- Verify Python 3.13+ is installed
- Check that all required files exist in the correct locations

**Invalid input errors:**
- Ensure task titles are not empty
- Verify task IDs exist before updating/deleting

**Memory errors:**
- The application stores data only in memory
- Data will be lost when the application exits
- This is expected behavior for Phase I

## Development Guidelines

### Code Organization

- Models in `src/models/` - Data structures only
- Store in `src/store/` - Data persistence (in-memory for Phase I)
- Services in `src/services/` - Business logic
- CLI in `src/cli/` - User interface

### Error Handling

- Always validate user input
- Provide clear error messages
- Handle missing tasks gracefully
- Prevent application crashes

### Best Practices

- Follow Python PEP 8 style guidelines
- Use type hints where appropriate
- Separate concerns between different modules
- Write clear, readable code
- Handle edge cases appropriately