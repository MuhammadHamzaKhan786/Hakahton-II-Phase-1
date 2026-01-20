"""
Task model for the Hackathon Todo Project - Phase I
Represents a single todo task with ID, title, and completion status.
"""

from typing import Optional


class Task:
    """
    Represents a todo task with ID, title, and completion status.

    Attributes:
        id (int): Unique identifier for the task
        title (str): The task description
        completed (bool): Whether the task is completed (default: False)
    """

    def __init__(self, task_id: int, title: str, completed: bool = False):
        """
        Initialize a new Task instance.

        Args:
            task_id (int): Unique identifier for the task
            title (str): The task description
            completed (bool): Whether the task is completed (default: False)

        Raises:
            ValueError: If title is empty or None
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        self.id = task_id
        self.title = title.strip()
        self.completed = completed

    def update_title(self, new_title: str) -> None:
        """
        Update the task title.

        Args:
            new_title (str): The new title for the task

        Raises:
            ValueError: If new_title is empty or None
        """
        if not new_title or not new_title.strip():
            raise ValueError("Task title cannot be empty")

        self.title = new_title.strip()

    def toggle_completion(self) -> bool:
        """
        Toggle the completion status of the task.

        Returns:
            bool: The new completion status
        """
        self.completed = not self.completed
        return self.completed

    def to_dict(self) -> dict:
        """
        Convert the task to a dictionary representation.

        Returns:
            dict: Dictionary representation of the task
        """
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed
        }

    def __str__(self) -> str:
        """
        String representation of the task.

        Returns:
            str: Formatted string representation
        """
        status = "✓" if self.completed else "○"
        return f"[{status}] {self.id}. {self.title}"

    def __repr__(self) -> str:
        """
        Detailed string representation of the task.

        Returns:
            str: Detailed string representation
        """
        return f"Task(id={self.id}, title='{self.title}', completed={self.completed})"