#!/usr/bin/env python3
"""
Todo Console Application - Data Models
This module defines the Task data model with validation.
"""


class Task:
    """Represents a todo task with validation"""

    def __init__(self, task_id, title, description="", completed=False):
        """
        Initialize a Task instance

        Args:
            task_id (int): Unique identifier for the task
            title (str): Title of the task (1-200 characters)
            description (str): Optional description (up to 1000 characters)
            completed (bool): Whether the task is completed (default: False)
        """
        self.id = task_id
        self.title = self._validate_title(title)
        self.description = self._validate_description(description)
        self.completed = completed

    def _validate_title(self, title):
        """Validate the title length (1-200 characters)"""
        if not isinstance(title, str):
            raise ValueError("Title must be a string")

        if len(title) < 1 or len(title) > 200:
            raise ValueError("Title must be between 1 and 200 characters")

        return title

    def _validate_description(self, description):
        """Validate the description length (up to 1000 characters)"""
        if not isinstance(description, str):
            raise ValueError("Description must be a string")

        if len(description) > 1000:
            raise ValueError("Description must be no more than 1000 characters")

        return description

    def to_dict(self):
        """Convert the task to a dictionary representation"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed
        }

    def __str__(self):
        """String representation of the task"""
        status = "✓" if self.completed else "○"
        return f"[{status}] {self.id}. {self.title}"

    def __repr__(self):
        """Developer-friendly representation of the task"""
        return f"Task(id={self.id}, title='{self.title}', completed={self.completed})"