"""
Demo script showing all Phase I functionality
"""
import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from src.services.task_service import TaskService

def demo_all_features():
    print("=== Phase I Demo: All Five Required Features ===\n")

    service = TaskService()

    # 1. Add Task
    print("1. ADD TASK FEATURE:")
    task1 = service.add_task("Buy groceries")
    task2 = service.add_task("Walk the dog")
    print(f"   Added task: '{task1.title}' with ID {task1.id}")
    print(f"   Added task: '{task2.title}' with ID {task2.id}")

    # 2. View Tasks
    print("\n2. VIEW TASKS FEATURE:")
    tasks = service.list_tasks()
    print("   Current tasks:")
    for task in tasks:
        status = "Completed" if task.completed else "Pending"
        print(f"   ID: {task.id} | Title: {task.title} | Status: {status}")

    # 3. Update Task
    print("\n3. UPDATE TASK FEATURE:")
    updated_task = service.update_task(1, "Buy food groceries")
    print(f"   Updated task {updated_task.id} to: '{updated_task.title}'")

    # 4. Mark Task as Complete
    print("\n4. MARK TASK AS COMPLETE FEATURE:")
    completed_task = service.toggle_completion(1)
    print(f"   Toggled completion for task {completed_task.id}: now {'Completed' if completed_task.completed else 'Pending'}")

    # 5. Delete Task
    print("\n5. DELETE TASK FEATURE:")
    delete_result = service.delete_task(2)
    print(f"   Deleted task ID 2: {'Success' if delete_result else 'Failed'}")

    # Show final state
    print("\n6. FINAL STATE:")
    remaining_tasks = service.list_tasks()
    if remaining_tasks:
        for task in remaining_tasks:
            status = "Completed" if task.completed else "Pending"
            print(f"   ID: {task.id} | Title: {task.title} | Status: {status}")
    else:
        print("   No tasks remaining")

    print(f"\n   Total tasks remaining: {len(remaining_tasks)}")
    print("\n=== Demo Complete ===")

if __name__ == "__main__":
    demo_all_features()