# Data Model: Hackathon Todo Project

**Date**: 2026-01-17
**Phase**: Phase I - In-Memory Python Console App
**Related**: specs/hackathon-todo/spec.md

## Overview

This document defines the data structures for the Hackathon Todo Project, starting with Phase I requirements and considering future phases.

## Phase I: In-Memory Data Model

### Task Entity

The core entity for the todo application:

```python
class Task:
    id: int (auto-generated, unique)
    title: str (required, non-empty)
    completed: bool (default: False)
```

**Attributes:**
- `id`: Unique identifier for the task, auto-generated when created
- `title`: The task description, required and must not be empty
- `completed`: Boolean indicating completion status, defaults to False

**Valid States:**
- Active task: `completed = False`
- Completed task: `completed = True`

**Operations:**
- Create: Generate new ID, set title, set completed=False
- Read: Access all attributes
- Update: Modify title, toggle completion status
- Delete: Remove from store

### In-Memory Storage Structure

Tasks will be stored in memory using a Python list or dictionary:

**Option 1: List-based storage**
```python
tasks: List[Task] = []
```

**Option 2: Dictionary-based storage (recommended)**
```python
tasks: Dict[int, Task] = {}
# Key: task.id, Value: Task object
```

Dictionary-based storage provides O(1) lookup time for operations by ID, which is more efficient for the required operations.

## Phase II+: Data Model Evolution

### User Entity (Phase II)

When authentication is introduced in Phase II, a User entity will be needed:

```python
class User:
    id: int (auto-generated, unique)
    username: str (unique)
    email: str (unique, validated)
    created_at: datetime
```

### Enhanced Task Entity (Phase II)

The Task entity will be extended to include user ownership:

```python
class Task:
    id: int (auto-generated, unique)
    title: str (required, non-empty)
    completed: bool (default: False)
    user_id: int (foreign key to User)
    created_at: datetime
    updated_at: datetime
```

### Database Schema (Phase II)

When persistent storage is introduced:

```sql
-- Users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tasks table
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    completed BOOLEAN DEFAULT FALSE,
    user_id INTEGER REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Data Validation Rules

### Phase I Validation
- Task title must be provided and non-empty
- Task ID must be unique within the store
- Task ID must be positive integer
- Update operations must target existing tasks
- Delete operations must target existing tasks

### Phase II+ Validation
- User authentication required for all operations
- Users can only access their own tasks
- Email format validation
- Username uniqueness validation

## Data Relationships

### Phase I
- Self-contained: No relationships needed

### Phase II+
- User (1) : Task (Many) relationship
- Each user can have multiple tasks
- Each task belongs to exactly one user
- Foreign key constraint ensures referential integrity

## Data Access Patterns

### Phase I Access Patterns
- Create: Add new task to store
- Read All: Retrieve all tasks in store
- Read One: Retrieve specific task by ID
- Update: Modify existing task by ID
- Delete: Remove task by ID

### Phase II+ Access Patterns
- User-specific: All operations scoped to authenticated user
- Filtering: Tasks filtered by user_id
- Authorization: Verify user owns accessed task

## Data Integrity

### Phase I Integrity Measures
- Unique ID generation to prevent conflicts
- Input validation to ensure data quality
- Error handling to prevent inconsistent state

### Phase II+ Integrity Measures
- Database constraints (foreign keys, unique constraints)
- Transaction management for complex operations
- Audit trails for tracking changes
- Soft deletes (optional) to maintain historical data

## Migration Considerations

When transitioning from Phase I to Phase II:
- Phase I in-memory data will not persist to Phase II database
- Clear documentation needed for users regarding data loss during upgrade
- Potential import functionality to migrate data if needed