#!/usr/bin/env python3
"""
Todo Console Application - Main Entry Point
This is the main application file that integrates all components.
"""

# Import the necessary modules
# from todo_manager import TodoManager
from .todo_manager import TodoManager
# from cli import TodoCLI
from .cli import TodoCLI



def main():
    """Main application entry point"""
    print("Welcome to the Todo Console Application!")

    # Initialize the todo manager and CLI
    todo_manager = TodoManager()
    cli = TodoCLI(todo_manager)

    # Start the main application loop
    cli.run()


if __name__ == "__main__":
    main()