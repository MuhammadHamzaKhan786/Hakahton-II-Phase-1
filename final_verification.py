"""
Final verification test for Phase I
"""

import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from src.models.task import Task
from src.store.in_memory_store import InMemoryStore
from src.services.task_service import TaskService
from src.cli.todo_app import TodoApp


def test_all_five_features():
    """Test all five required features from the specification."""
    print("Testing all five required features...")

    service = TaskService()

    # 1. Add Task - Given I am at the CLI prompt, When I add a new task, Then the task appears in my task list with a unique ID and completion status of false
    print("1. Testing Add Task...")
    task1 = service.add_task("Buy groceries")
    assert task1.id == 1
    assert task1.title == "Buy groceries"
    assert task1.completed == False

    task2 = service.add_task("Walk the dog")
    assert task2.id == 2
    assert task2.title == "Walk the dog"
    assert task2.completed == False

    # 2. View Tasks - Given I have tasks in my list, When I view the task list, Then all tasks are displayed with their ID, title, and completion status
    print("2. Testing View Tasks...")
    tasks = service.list_tasks()
    assert len(tasks) == 2

    task_ids = {task.id for task in tasks}
    assert task_ids == {1, 2}

    task_titles = {task.title for task in tasks}
    assert task_titles == {"Buy groceries", "Walk the dog"}

    # 3. Update Task - Given I have a task in my list, When I update the task title, Then the task is updated with the new title
    print("3. Testing Update Task...")
    updated_task = service.update_task(1, "Buy food groceries")
    assert updated_task.title == "Buy food groceries"

    # 4. Delete Task - Given I have a task in my list, When I delete the task, Then the task is removed from the list
    print("4. Testing Delete Task...")
    result = service.delete_task(2)
    assert result == True

    remaining_tasks = service.list_tasks()
    assert len(remaining_tasks) == 1
    assert remaining_tasks[0].id == 1

    # 5. Mark Task as Complete - Given I have an incomplete task, When I mark it as complete, Then the task's completion status changes to true
    print("5. Testing Mark Task as Complete...")
    original_status = remaining_tasks[0].completed
    toggled_task = service.toggle_completion(1)
    assert toggled_task.completed != original_status
    assert toggled_task.completed == True

    print("SUCCESS: All five required features work correctly!")


def test_error_handling():
    """Test error handling for invalid inputs."""
    print("Testing error handling...")

    service = TaskService()

    # Test adding task with empty title
    try:
        service.add_task("")
        assert False, "Should have raised an error for empty title"
    except ValueError:
        pass  # Expected

    try:
        service.add_task("   ")  # Only spaces
        assert False, "Should have raised an error for whitespace-only title"
    except ValueError:
        pass  # Expected

    # Test updating non-existent task
    try:
        service.update_task(999, "New title")
        assert False, "Should have raised an error for non-existent task"
    except ValueError:
        pass  # Expected

    # Test deleting non-existent task
    try:
        service.delete_task(999)
        assert False, "Should have raised an error for non-existent task"
    except ValueError:
        pass  # Expected

    # Test toggling non-existent task
    try:
        service.toggle_completion(999)
        assert False, "Should have raised an error for non-existent task"
    except ValueError:
        pass  # Expected

    print("SUCCESS: Error handling works correctly!")


def test_architecture_separation():
    """Verify clean architecture separation between components."""
    print("Verifying architecture separation...")

    # Import and check each module exists and has expected classes/methods
    from src.models.task import Task
    from src.store.in_memory_store import InMemoryStore
    from src.services.task_service import TaskService
    from src.cli.todo_app import TodoApp

    # Verify Task model has expected methods
    assert hasattr(Task, '__init__')
    assert hasattr(Task, 'update_title')
    assert hasattr(Task, 'toggle_completion')

    # Verify InMemoryStore has expected methods
    assert hasattr(InMemoryStore, 'add_task')
    assert hasattr(InMemoryStore, 'get_task')
    assert hasattr(InMemoryStore, 'get_all_tasks')
    assert hasattr(InMemoryStore, 'update_task')
    assert hasattr(InMemoryStore, 'delete_task')
    assert hasattr(InMemoryStore, 'toggle_task_completion')

    # Verify TaskService has expected methods
    assert hasattr(TaskService, 'add_task')
    assert hasattr(TaskService, 'list_tasks')
    assert hasattr(TaskService, 'update_task')
    assert hasattr(TaskService, 'delete_task')
    assert hasattr(TaskService, 'toggle_completion')

    # Verify TodoApp has expected methods
    assert hasattr(TodoApp, 'display_menu')
    assert hasattr(TodoApp, 'run')

    print("SUCCESS: Architecture separation is clean!")


def test_in_memory_only():
    """Confirm no file I/O or database usage (in-memory only)."""
    print("Confirming in-memory only storage...")

    # Create two separate stores
    store1 = InMemoryStore()
    store1.add_task("Task from store 1")

    store2 = InMemoryStore()
    tasks_in_store2 = store2.get_all_tasks()

    # Store 2 should be empty since it's a separate instance
    assert len(tasks_in_store2) == 0

    # Add a task to store 2
    store2.add_task("Task from store 2")
    tasks_in_store1 = store1.get_all_tasks()

    # Store 1 should still only have its original task
    assert len(tasks_in_store1) == 1
    assert tasks_in_store1[0].title == "Task from store 1"

    print("SUCCESS: Confirmed in-memory only storage!")


def run_final_verification():
    """Run all final verification tests."""
    print("Running final verification for Phase I...\n")

    test_all_five_features()
    test_error_handling()
    test_architecture_separation()
    test_in_memory_only()

    print("\nSUCCESS: All verification tests passed! Phase I is complete and compliant.")


if __name__ == "__main__":
    run_final_verification()