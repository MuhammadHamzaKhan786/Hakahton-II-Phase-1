"""
Task service for the Hackathon Todo Project - Phase I
Provides business logic for task operations with validation and error handling.
"""

from typing import List, Optional
from src.models.task import Task
from src.store.in_memory_store import InMemoryStore


class TaskService:
    """
    Provides business logic for task operations.

    This class handles task operations with validation and error handling,
    coordinating between the Task model and the InMemoryStore.
    """

    def __init__(self):
        """Initialize the task service with an in-memory store."""
        self.store = InMemoryStore()

    def add_task(self, title: str) -> Optional[Task]:
        """
        Add a new task with validation.

        Args:
            title (str): The title of the task to add

        Returns:
            Optional[Task]: The created task if successful, None if invalid input

        Raises:
            ValueError: If title is empty or None
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty or None")

        return self.store.add_task(title)

    def list_tasks(self) -> List[Task]:
        """
        List all tasks in the store.

        Returns:
            List[Task]: A list of all tasks
        """
        return self.store.get_all_tasks()

    def update_task(self, task_id: int, new_title: str) -> Optional[Task]:
        """
        Update a task with validation.

        Args:
            task_id (int): The ID of the task to update
            new_title (str): The new title for the task

        Returns:
            Optional[Task]: The updated task if successful, None if task not found

        Raises:
            ValueError: If new_title is empty or None
        """
        if not new_title or not new_title.strip():
            raise ValueError("Task title cannot be empty or None")

        updated_task = self.store.update_task(task_id, new_title)
        if updated_task is None:
            raise ValueError(f"Task with ID {task_id} not found")

        return updated_task

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task with validation.

        Args:
            task_id (int): The ID of the task to delete

        Returns:
            bool: True if the task was deleted, False if not found
        """
        if task_id <= 0:
            raise ValueError("Task ID must be a positive integer")

        task_exists = self.store.get_task(task_id) is not None
        if not task_exists:
            raise ValueError(f"Task with ID {task_id} not found")

        return self.store.delete_task(task_id)

    def toggle_completion(self, task_id: int) -> Optional[Task]:
        """
        Toggle the completion status of a task.

        Args:
            task_id (int): The ID of the task to toggle

        Returns:
            Optional[Task]: The updated task if successful, None if task not found
        """
        if task_id <= 0:
            raise ValueError("Task ID must be a positive integer")

        task = self.store.toggle_task_completion(task_id)
        if task is None:
            raise ValueError(f"Task with ID {task_id} not found")

        return task

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a specific task by its ID.

        Args:
            task_id (int): The ID of the task to retrieve

        Returns:
            Optional[Task]: The task if found, None otherwise
        """
        if task_id <= 0:
            raise ValueError("Task ID must be a positive integer")

        return self.store.get_task(task_id)