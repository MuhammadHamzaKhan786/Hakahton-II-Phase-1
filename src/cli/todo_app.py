"""
CLI application for the Hackathon Todo Project - Phase I
Provides a command-line interface for managing tasks.
"""

import sys
from typing import Optional
from src.services.task_service import TaskService


class TodoApp:
    """
    Command-line interface for the Todo application.

    This class manages the user interaction loop and delegates
    task operations to the TaskService.
    """

    def __init__(self):
        """Initialize the CLI application with a task service."""
        self.service = TaskService()
        self.running = True

    def display_menu(self):
        """Display the main menu options."""
        print("\n=== Todo App ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Toggle Completion")
        print("6. Exit")
        print("===============")

    def get_user_choice(self) -> str:
        """
        Get user's menu choice.

        Returns:
            str: The user's choice as a string
        """
        try:
            return input("Choose an option (1-6): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            return "6"

    def handle_add_task(self):
        """Handle the add task operation."""
        try:
            title = input("Enter task title: ").strip()

            if not title:
                print("Error: Task title cannot be empty.")
                return

            task = self.service.add_task(title)
            print(f"Task added with ID: {task.id}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def handle_view_tasks(self):
        """Handle the view tasks operation."""
        try:
            tasks = self.service.list_tasks()

            if not tasks:
                print("No tasks found.")
                return

            print("\nYour Tasks:")
            for task in tasks:
                status = "Completed" if task.completed else "Pending"
                print(f"ID: {task.id} | Title: {task.title} | Status: {status}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def handle_update_task(self):
        """Handle the update task operation."""
        try:
            task_id_str = input("Enter task ID to update: ").strip()

            if not task_id_str.isdigit():
                print("Error: Task ID must be a number.")
                return

            task_id = int(task_id_str)
            if task_id <= 0:
                print("Error: Task ID must be a positive number.")
                return

            new_title = input("Enter new title: ").strip()

            if not new_title:
                print("Error: New title cannot be empty.")
                return

            task = self.service.update_task(task_id, new_title)
            print(f"Task {task.id} updated successfully!")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def handle_delete_task(self):
        """Handle the delete task operation."""
        try:
            task_id_str = input("Enter task ID to delete: ").strip()

            if not task_id_str.isdigit():
                print("Error: Task ID must be a number.")
                return

            task_id = int(task_id_str)
            if task_id <= 0:
                print("Error: Task ID must be a positive number.")
                return

            success = self.service.delete_task(task_id)
            if success:
                print(f"Task {task_id} deleted successfully!")
            else:
                print(f"Error: Task with ID {task_id} not found.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def handle_toggle_completion(self):
        """Handle the toggle completion operation."""
        try:
            task_id_str = input("Enter task ID to toggle completion: ").strip()

            if not task_id_str.isdigit():
                print("Error: Task ID must be a number.")
                return

            task_id = int(task_id_str)
            if task_id <= 0:
                print("Error: Task ID must be a positive number.")
                return

            task = self.service.toggle_completion(task_id)
            if task:
                status = "completed" if task.completed else "pending"
                print(f"Task {task.id} is now {status}!")
            else:
                print(f"Error: Task with ID {task_id} not found.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def handle_exit(self):
        """Handle the exit operation."""
        print("Goodbye!")
        self.running = False

    def run(self):
        """Run the main application loop."""
        print("Welcome to the Todo App!")

        while self.running:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == "1":
                self.handle_add_task()
            elif choice == "2":
                self.handle_view_tasks()
            elif choice == "3":
                self.handle_update_task()
            elif choice == "4":
                self.handle_delete_task()
            elif choice == "5":
                self.handle_toggle_completion()
            elif choice == "6":
                self.handle_exit()
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")


def main():
    """Main entry point for the application."""
    app = TodoApp()
    app.run()


if __name__ == "__main__":
    main()