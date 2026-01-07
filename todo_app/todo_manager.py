#!/usr/bin/env python3
"""
Todo Console Application - Todo Manager
This module handles all core business logic for task management.
"""
# from models import Task
from .models import Task



class TodoManager:
    """Manages todo tasks with in-memory storage"""

    def __init__(self):
        """Initialize the todo manager with empty storage"""
        self._tasks = []
        self._next_id = 1

    def _generate_id(self):
        """Generate the next available ID"""
        new_id = self._next_id
        self._next_id += 1
        return new_id

    def add_task(self, title, description=""):
        """
        Add a new task to the todo list

        Args:
            title (str): Title of the task (1-200 characters)
            description (str): Optional description (up to 1000 characters)

        Returns:
            Task: The newly created task
        """
        task_id = self._generate_id()
        task = Task(task_id, title, description, completed=False)
        self._tasks.append(task)
        return task

    def get_all_tasks(self):
        """
        Get all tasks in the todo list

        Returns:
            list: List of all Task objects
        """
        return self._tasks.copy()

    def get_task_by_id(self, task_id):
        """
        Get a specific task by its ID

        Args:
            task_id (int): The ID of the task to retrieve

        Returns:
            Task: The task with the specified ID

        Raises:
            ValueError: If no task with the given ID exists
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        raise ValueError(f"No task found with ID {task_id}")

    def update_task(self, task_id, title=None, description=None):
        """
        Update an existing task

        Args:
            task_id (int): The ID of the task to update
            title (str, optional): New title for the task
            description (str, optional): New description for the task

        Returns:
            Task: The updated task

        Raises:
            ValueError: If no task with the given ID exists
        """
        task = self.get_task_by_id(task_id)

        # Use current values if new values are not provided
        new_title = title if title is not None else task.title
        new_description = description if description is not None else task.description

        # Validate the new values
        updated_task = Task(task_id, new_title, new_description, task.completed)

        # Update the task in the list
        index = self._tasks.index(task)
        self._tasks[index] = updated_task

        return updated_task

    def delete_task(self, task_id):
        """
        Delete a task by its ID

        Args:
            task_id (int): The ID of the task to delete

        Returns:
            bool: True if the task was deleted, False if it didn't exist

        Raises:
            ValueError: If no task with the given ID exists
        """
        task = self.get_task_by_id(task_id)
        self._tasks.remove(task)
        return True

    def mark_completed(self, task_id):
        """
        Mark a task as completed

        Args:
            task_id (int): The ID of the task to mark as completed

        Returns:
            Task: The updated task

        Raises:
            ValueError: If no task with the given ID exists
        """
        task = self.get_task_by_id(task_id)
        task.completed = True
        return task

    def get_next_id(self):
        """
        Get the next available ID without incrementing it

        Returns:
            int: The next available ID
        """
        return self._next_id