#!/usr/bin/env python3
"""
Test script for the Todo Console Application
This script tests all the main functionality of the application.
"""
import sys
import os

# Add the current directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'todo-app'))

from todo_manager import TodoManager
from models import Task


def test_task_creation():
    """Test Task model creation and validation"""
    print("Testing Task creation and validation...")

    # Test valid task creation
    task = Task(1, "Test title", "Test description")
    assert task.id == 1
    assert task.title == "Test title"
    assert task.description == "Test description"
    assert task.completed == False
    print("+ Valid task creation works")

    # Test title validation (too short)
    try:
        Task(2, "", "Description")
        assert False, "Should have raised an error for empty title"
    except ValueError:
        print("+ Title validation (empty) works")

    # Test title validation (too long)
    try:
        Task(2, "a" * 201, "Description")
        assert False, "Should have raised an error for title too long"
    except ValueError:
        print("+ Title validation (too long) works")

    # Test description validation (too long)
    try:
        Task(2, "Valid title", "a" * 1001)
        assert False, "Should have raised an error for description too long"
    except ValueError:
        print("+ Description validation (too long) works")


def test_todo_manager():
    """Test TodoManager functionality"""
    print("\nTesting TodoManager functionality...")

    manager = TodoManager()

    # Test adding a task
    task = manager.add_task("Test task", "Test description")
    assert task.id == 1
    assert task.title == "Test task"
    print("+ Adding task works")

    # Test getting all tasks
    tasks = manager.get_all_tasks()
    assert len(tasks) == 1
    assert tasks[0].id == 1
    print("+ Getting all tasks works")

    # Test getting task by ID
    retrieved_task = manager.get_task_by_id(1)
    assert retrieved_task.id == 1
    assert retrieved_task.title == "Test task"
    print("+ Getting task by ID works")

    # Test updating task
    updated_task = manager.update_task(1, "Updated title", "Updated description")
    assert updated_task.title == "Updated title"
    assert updated_task.description == "Updated description"
    print("+ Updating task works")

    # Test marking as completed
    completed_task = manager.mark_completed(1)
    assert completed_task.completed == True
    print("+ Marking task as completed works")

    # Test deleting task
    manager.delete_task(1)
    assert len(manager.get_all_tasks()) == 0
    print("+ Deleting task works")

    # Test error when getting non-existent task
    try:
        manager.get_task_by_id(999)
        assert False, "Should have raised an error for non-existent task"
    except ValueError:
        print("+ Error handling for non-existent task works")


def run_integration_test():
    """Run a full integration test of the application flow"""
    print("\nRunning integration test...")

    # Create a todo manager
    manager = TodoManager()

    # Add several tasks
    task1 = manager.add_task("Buy groceries", "Milk, bread, eggs")
    task2 = manager.add_task("Walk the dog", "In the park for 30 minutes")
    task3 = manager.add_task("Finish report", "Complete the quarterly report")

    # Verify all tasks were added
    all_tasks = manager.get_all_tasks()
    assert len(all_tasks) == 3
    print("+ Added 3 tasks successfully")

    # Mark one task as completed
    manager.mark_completed(task1.id)
    completed_task = manager.get_task_by_id(task1.id)
    assert completed_task.completed == True
    print("+ Marked first task as completed")

    # Update a task
    updated_task = manager.update_task(task2.id, "Walk the cat", "Play with the cat instead")
    assert updated_task.title == "Walk the cat"
    print("+ Updated second task successfully")

    # Delete a task
    manager.delete_task(task3.id)
    remaining_tasks = manager.get_all_tasks()
    assert len(remaining_tasks) == 2
    print("+ Deleted third task successfully")

    print("+ Integration test passed!")


def main():
    """Run all tests"""
    print("Starting Todo Application Tests...\n")

    try:
        test_task_creation()
        test_todo_manager()
        run_integration_test()

        print("\nAll tests passed! The Todo application is working correctly.")
    except Exception as e:
        print(f"\nTest failed with error: {e}")
        import traceback
        traceback.print_exc()
        return 1

    return 0


if __name__ == "__main__":
    exit(main())