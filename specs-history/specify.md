# Todo In-Memory Python Console App - Specification

## Project Overview
A simple console-based todo application built in Python that operates entirely in memory with no persistent storage. The application allows users to manage their tasks through a command-line interface with a menu-driven system.

## User Scenarios
- As a user, I want to add new tasks with a title and optional description so that I can keep track of my responsibilities
- As a user, I want to view all my tasks so that I can see what needs to be done
- As a user, I want to mark tasks as completed so that I can track my progress
- As a user, I want to delete tasks that are no longer needed
- As a user, I want to edit existing tasks to update their information
- As a user, I want clear error messages when I enter invalid input so that I can correct my mistakes

## Functional Requirements
1. The application must provide a main menu with 6 options for task management
2. The application must store tasks in memory using a list of dictionaries
3. Each task must have an auto-incrementing ID, title (1-200 characters), optional description (up to 1000 characters), and completed status
4. The application must validate user inputs and handle invalid entries gracefully
5. The application must continue running until the user selects the exit option
6. All errors must be handled gracefully with clear, user-friendly messages

## Success Criteria
- Users can successfully add, view, update, and delete tasks through the console interface
- The application maintains responsiveness after any error occurs
- All user inputs are validated with appropriate error messages for invalid entries
- Task data is properly managed in memory with correct field types and constraints
- The console interface provides a clear and intuitive menu system

## Key Entities
- Task: The core data structure containing ID, title, description, and completion status
- Menu System: The console interface that provides the 6 main options for task management
- In-Memory Storage: The list of dictionaries that holds all task data during application runtime

## Constraints
- Python 3.13+ must be used
- Only standard library modules are allowed (no external dependencies)
- Data is not persisted across application restarts
- Task titles must be between 1-200 characters
- Task descriptions are optional and limited to 1000 characters