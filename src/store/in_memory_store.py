"""
In-memory storage for the Hackathon Todo Project - Phase I
Stores tasks in runtime memory with CRUD operations.
"""

from typing import Dict, List, Optional
from src.models.task import Task


class InMemoryStore:
    """
    Implements in-memory storage for tasks.

    This class provides basic CRUD operations for Task objects,
    storing them in memory during the application lifecycle.
    """

    def __init__(self):
        """Initialize the in-memory store with an empty task dictionary."""
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, title: str) -> Task:
        """
        Add a new task to the store.

        Args:
            title (str): The title of the task

        Returns:
            Task: The created Task object with assigned ID

        Raises:
            ValueError: If title is empty
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        task_id = self._next_id
        self._next_id += 1

        task = Task(task_id=task_id, title=title)
        self._tasks[task_id] = task

        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Retrieve a task by its ID.

        Args:
            task_id (int): The ID of the task to retrieve

        Returns:
            Optional[Task]: The task if found, None otherwise
        """
        return self._tasks.get(task_id)

    def get_all_tasks(self) -> List[Task]:
        """
        Retrieve all tasks in the store.

        Returns:
            List[Task]: A list of all tasks in the store
        """
        return list(self._tasks.values())

    def update_task(self, task_id: int, new_title: str) -> Optional[Task]:
        """
        Update the title of an existing task.

        Args:
            task_id (int): The ID of the task to update
            new_title (str): The new title for the task

        Returns:
            Optional[Task]: The updated task if successful, None if task not found

        Raises:
            ValueError: If new_title is empty
        """
        if not new_title or not new_title.strip():
            raise ValueError("Task title cannot be empty")

        task = self._tasks.get(task_id)
        if task:
            task.update_title(new_title)
            return task
        return None

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task from the store.

        Args:
            task_id (int): The ID of the task to delete

        Returns:
            bool: True if the task was deleted, False if not found
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False

    def toggle_task_completion(self, task_id: int) -> Optional[Task]:
        """
        Toggle the completion status of a task.

        Args:
            task_id (int): The ID of the task to toggle

        Returns:
            Optional[Task]: The updated task if successful, None if task not found
        """
        task = self._tasks.get(task_id)
        if task:
            task.toggle_completion()
            return task
        return None

    def get_next_available_id(self) -> int:
        """
        Get the next available ID for a new task.

        Returns:
            int: The next available task ID
        """
        return self._next_id