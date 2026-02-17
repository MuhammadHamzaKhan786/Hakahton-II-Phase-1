# Hackathon Todo Project

A multi-phase todo application that evolves from a minimal in-memory CLI app to a cloud-deployed, AI-powered system.

## Overview

The Hackathon Todo Project is a five-phase application that demonstrates progressive enhancement of a todo management system. Starting with a simple CLI application in Phase I, it will eventually become a full-featured web application with AI capabilities, containerized deployment, and cloud infrastructure.

### Current Phase

**Phase I: In-Memory Python Console App**

This is the foundational phase that provides core todo management functionality through a command-line interface. All data is stored in memory and will be lost when the application closes.

## Features

- **Add Task** - Create new todo items with auto-generated IDs
- **View Tasks** - Display all tasks with their completion status
- **Update Task** - Modify existing task titles
- **Delete Task** - Remove tasks from the list
- **Toggle Completion** - Mark tasks as complete/incomplete

## Project Structure

```
todo-cli/
├── src/
│   ├── cli/
│   │   └── todo_app.py          # CLI application entry point
│   ├── models/
│   │   └── task.py              # Task data model
│   ├── services/
│   │   └── task_service.py      # Business logic layer
│   └── store/
│       └── in_memory_store.py   # In-memory data storage
├── specs/
│   └── hackathon-todo/
│       ├── spec.md               # Feature specifications
│       ├── quickstart.md         # Quick start guide
│       └── research.md           # Research notes
├── demo_phase_i.py              # Demo script
├── test_phase_i.py              # Unit tests
├── USER_GUIDE.md                # Detailed user guide
└── HOW_TO_USE.md                # Quick usage reference
```

## Requirements

- **Python 3.13+** (or Python 3.x with basic standard library)
- No external dependencies required for Phase I

## Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd todo-cli
   ```

## Usage

Run the CLI application:

```bash
python -m src.cli.todo_app
```

Or alternatively:

```bash
python src/cli/todo_app.py
```

### Interactive Menu

The application presents an interactive menu:

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

### Example Workflow

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
Enter task title: Buy groceries
Task added with ID: 1

Choose an option (1-6): 2

Your Tasks:
ID: 1 | Title: Buy groceries | Status: Pending

Choose an option (1-6): 5
Enter task ID to toggle completion: 1
Task 1 is now completed!

Choose an option (1-6): 6
Goodbye!
```

## Running Tests

Execute the test suite:

```bash
python -m pytest test_phase_i.py
```

Or run the demo script:

```bash
python demo_phase_i.py
```

## Architecture

The project follows clean architecture principles with clear separation of concerns:

- **Models** (`src/models/`) - Data structures representing domain entities
- **Services** (`src/services/`) - Business logic and operations
- **Store** (`src/store/`) - Data persistence layer (in-memory for Phase I)
- **CLI** (`src/cli/`) - User interface and interaction handling

## Future Phases

This project will evolve through five phases:

| Phase | Description |
|-------|-------------|
| Phase I | In-Memory Python Console App (Current) |
| Phase II | Web-based Todo with Authentication & Database |
| Phase III | AI-Powered Natural Language Task Management |
| Phase IV | Containerized Deployment (Kubernetes) |
| Phase V | Production Cloud Deployment |

## License

This project is available for educational and demonstration purposes.

## Contributing

This is a learning project that demonstrates progressive software development. Feel free to explore, modify, and extend it as needed.
