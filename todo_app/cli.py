#!/usr/bin/env python3
"""
Todo Console Application - CLI Interface
This module handles the console interface and user interaction.
"""


class TodoCLI:
    """Handles console interface and user interaction"""

    def __init__(self, todo_manager):
        """
        Initialize the CLI interface

        Args:
            todo_manager (TodoManager): The todo manager instance to use
        """
        self.todo_manager = todo_manager

    def display_menu(self):
        """Display the main menu options"""
        print("\n" + "="*40)
        print("TODO CONSOLE APPLICATION")
        print("="*40)
        print("1. Add a new task")
        print("2. List all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Mark task as completed")
        print("6. Exit")
        print("="*40)

    def get_user_choice(self):
        """
        Get and validate user's menu choice

        Returns:
            str: The user's choice (1-6)
        """
        while True:
            try:
                choice = input("Enter your choice (1-6): ").strip()
                if choice in ['1', '2', '3', '4', '5', '6']:
                    return choice
                else:
                    print("Invalid choice. Please enter a number between 1 and 6.")
            except KeyboardInterrupt:
                print("\nGoodbye!")
                return '6'  # Return exit choice
            except EOFError:
                print("\nGoodbye!")
                return '6'  # Return exit choice

    def get_task_input(self, existing_title=None, existing_description=None):
        """
        Get task input from the user

        Args:
            existing_title (str, optional): Existing title to prefill
            existing_description (str, optional): Existing description to prefill

        Returns:
            tuple: (title, description) entered by the user
        """
        # Get title
        if existing_title:
            title_input = input(f"Enter task title (current: '{existing_title}'): ").strip()
            title = title_input if title_input else existing_title
        else:
            while True:
                title = input("Enter task title (1-200 characters): ").strip()
                if title:
                    break
                print("Title cannot be empty. Please enter a title.")

        # Get description
        if existing_description is not None:
            description_input = input(f"Enter task description (current: '{existing_description}'): ").strip()
            description = description_input if description_input else existing_description
        else:
            description = input("Enter task description (optional, max 1000 characters): ").strip()

        return title, description

    def display_tasks(self):
        """Display all tasks in a formatted way"""
        tasks = self.todo_manager.get_all_tasks()

        if not tasks:
            print("\nNo tasks found.")
            return

        print(f"\nYour tasks ({len(tasks)} total):")
        print("-" * 50)
        for task in tasks:
            print(f"  {task}")
            if task.description:
                print(f"      Description: {task.description}")
        print("-" * 50)

    def handle_add_task(self):
        """Handle adding a new task"""
        try:
            print("\n--- Add New Task ---")
            title, description = self.get_task_input()
            task = self.todo_manager.add_task(title, description)
            print(f"Task added successfully! ID: {task.id}")
        except ValueError as e:
            print(f"Error adding task: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def handle_list_tasks(self):
        """Handle listing all tasks"""
        print("\n--- All Tasks ---")
        self.display_tasks()

    def handle_update_task(self):
        """Handle updating an existing task"""
        try:
            print("\n--- Update Task ---")
            self.display_tasks()

            if not self.todo_manager.get_all_tasks():
                return

            task_id = int(input("Enter the ID of the task to update: "))
            task = self.todo_manager.get_task_by_id(task_id)

            print(f"Updating task: {task}")
            title, description = self.get_task_input(task.title, task.description)
            updated_task = self.todo_manager.update_task(task_id, title, description)
            print(f"Task updated successfully!")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def handle_delete_task(self):
        """Handle deleting a task"""
        try:
            print("\n--- Delete Task ---")
            self.display_tasks()

            if not self.todo_manager.get_all_tasks():
                return

            task_id = int(input("Enter the ID of the task to delete: "))
            task = self.todo_manager.get_task_by_id(task_id)
            print(f"You are about to delete: {task}")
            confirm = input("Are you sure? (y/N): ").strip().lower()

            if confirm in ['y', 'yes']:
                self.todo_manager.delete_task(task_id)
                print("Task deleted successfully!")
            else:
                print("Deletion cancelled.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def handle_mark_completed(self):
        """Handle marking a task as completed"""
        try:
            print("\n--- Mark Task as Completed ---")
            self.display_tasks()

            if not self.todo_manager.get_all_tasks():
                return

            task_id = int(input("Enter the ID of the task to mark as completed: "))
            task = self.todo_manager.get_task_by_id(task_id)
            completed_task = self.todo_manager.mark_completed(task_id)
            print(f"Task marked as completed: {completed_task}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def run(self):
        """Run the main application loop"""
        print("Todo Console Application started. Press Ctrl+C to exit.")

        while True:
            try:
                self.display_menu()
                choice = self.get_user_choice()

                if choice == '1':
                    self.handle_add_task()
                elif choice == '2':
                    self.handle_list_tasks()
                elif choice == '3':
                    self.handle_update_task()
                elif choice == '4':
                    self.handle_delete_task()
                elif choice == '5':
                    self.handle_mark_completed()
                elif choice == '6':
                    print("Thank you for using the Todo Console Application. Goodbye!")
                    break
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                print("The application will continue running.")