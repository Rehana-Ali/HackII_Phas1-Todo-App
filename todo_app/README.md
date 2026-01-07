# Todo Console Application

A simple in-memory todo application built with Python using only standard library modules.

## Features

- Add new tasks with titles and descriptions
- List all tasks with completion status
- Update existing tasks
- Delete tasks
- Mark tasks as completed
- Simple console-based menu interface

## Requirements

- Python 3.13 or higher

## Usage

1. Make sure you have Python 3.13+ installed
2. Run the application:
   ```bash
   python main.py
   ```
3. Follow the on-screen menu prompts to manage your tasks

## Menu Options

1. **Add a new task** - Create a new todo item
2. **List all tasks** - View all current tasks with their status
3. **Update a task** - Modify an existing task's title or description
4. **Delete a task** - Remove a task from your list
5. **Mark task as completed** - Update a task's status to completed
6. **Exit** - Quit the application

## Data Persistence

This application stores all data in memory only. All tasks will be lost when the application exits.

## Architecture

- `main.py` - Application entry point and main loop
- `models.py` - Task data model with validation
- `todo_manager.py` - Core business logic for task management
- `cli.py` - Console interface and user interaction