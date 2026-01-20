"""
Test script to verify all Phase I functionality
"""

import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from src.models.task import Task
from src.store.in_memory_store import InMemoryStore
from src.services.task_service import TaskService


def test_task_model():
    """Test the Task model functionality."""
    print("Testing Task model...")

    # Test creating a task
    task = Task(1, "Test task")
    assert task.id == 1
    assert task.title == "Test task"
    assert task.completed == False

    # Test updating title
    task.update_title("Updated test task")
    assert task.title == "Updated test task"

    # Test toggling completion
    task.toggle_completion()
    assert task.completed == True
    task.toggle_completion()
    assert task.completed == False

    print("SUCCESS: Task model tests passed")


def test_in_memory_store():
    """Test the in-memory store functionality."""
    print("Testing in-memory store...")

    store = InMemoryStore()

    # Test adding a task
    task = store.add_task("Test task")
    assert task.id == 1
    assert task.title == "Test task"

    # Test getting a task
    retrieved_task = store.get_task(1)
    assert retrieved_task is not None
    assert retrieved_task.id == 1

    # Test getting all tasks
    all_tasks = store.get_all_tasks()
    assert len(all_tasks) == 1

    # Test updating a task
    updated_task = store.update_task(1, "Updated task")
    assert updated_task is not None
    assert updated_task.title == "Updated task"

    # Test toggling completion
    toggled_task = store.toggle_task_completion(1)
    assert toggled_task is not None
    assert toggled_task.completed == True

    # Test deleting a task
    deleted = store.delete_task(1)
    assert deleted == True

    print("SUCCESS: In-memory store tests passed")


def test_task_service():
    """Test the task service functionality."""
    print("Testing task service...")

    service = TaskService()

    # Test adding a task
    task = service.add_task("Test task")
    assert task is not None
    assert task.id == 1
    assert task.title == "Test task"

    # Test listing tasks
    tasks = service.list_tasks()
    assert len(tasks) == 1

    # Test updating a task
    updated_task = service.update_task(1, "Updated task")
    assert updated_task is not None
    assert updated_task.title == "Updated task"

    # Test toggling completion
    toggled_task = service.toggle_completion(1)
    assert toggled_task is not None
    assert toggled_task.completed == True

    # Test deleting a task
    deleted = service.delete_task(1)
    assert deleted == True

    # Test error handling
    try:
        service.update_task(999, "Non-existent task")
        assert False, "Should have raised an error"
    except ValueError:
        pass  # Expected

    try:
        service.delete_task(999)
        assert False, "Should have raised an error"
    except ValueError:
        pass  # Expected

    print("SUCCESS: Task service tests passed")


def run_tests():
    """Run all tests."""
    print("Running Phase I functionality tests...\n")

    test_task_model()
    test_in_memory_store()
    test_task_service()

    print("\nSUCCESS: All tests passed! Phase I functionality is working correctly.")


if __name__ == "__main__":
    run_tests()