import os
import csv

class Task:
    def __init__(self, title, description, category, completed=False):
        # Initialize a new task with title, description, category, and completion status
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed

    def mark_completed(self):
        # Mark the task as completed
        self.completed = True

def opentaskfile():
    # Create a new task file if it doesn't exist
    try:
        if not os.path.exists('taskfile.csv'):
            with open('taskfile.csv', 'w') as file:
                file.write('Title,Description,Category,Status\n')  # Write header
    except Exception as e:
        print(f"Error opening task file: {e}")

def load_tasks_from_file(file_path):
    # Load tasks from the CSV file
    tasks = []
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                tasks = file.read().splitlines()  # Read all lines
    except Exception as e:
        print(f"Error loading tasks from file: {e}")
    return tasks

def save_tasks_to_file(file_path, tasks):
    # Save the current list of tasks back to the CSV file
    try:
        with open(file_path, 'w') as file:
            for task in tasks:
                file.write(f"{task}\n")  # Write each task on a new line
    except Exception as e:
        print(f"Error saving tasks to file: {e}")

def mark_task_completed(file_path):
    # Mark a specific task as completed based on user input
    tasks = load_tasks_from_file(file_path)
    title = input("Enter the title of the task to mark as completed: ")
    updated_tasks = []
    task_found = False

    for task in tasks:
        task_details = task.split(',')
        if task_details[0] == title:
            if task_details[-1].strip() != 'completed':
                task_details[-1] = 'completed'  # Update status to 'completed'
                task_found = True
                print(f"Task '{title}' marked as completed.")
            else:
                print(f"Task '{title}' is already completed.")
        updated_tasks.append(','.join(task_details))  # Reconstruct the task line
    
    if not task_found:
        print("Task not found.")
    
    save_tasks_to_file(file_path, updated_tasks)  # Save updated tasks

def delete_task(title):
    # Delete a task based on the title provided by the user
    try:
        lines = []
        with open('taskfile.csv', 'r') as file:
            lines = file.readlines()  # Read all lines
        with open('taskfile.csv', 'w') as file:
            for line in lines:
                if not line.startswith(title + ','):
                    file.write(line)  # Write back all lines except the one to delete
        print("Deleted successfully")
    except Exception as e:
        print(f"Error deleting task: {e}")

def add_task(title, description, category, status=''):
    # Add a new task to the CSV file
    try:
        with open('taskfile.csv', 'a') as file:
            file.write(f"{title},{description},{category},{status}\n")  # Append new task
        print("Task added")
    except Exception as e:
        print(f"Error adding task: {e}")

def view_task():
    # Display all tasks in the CSV file
    try:
        with open('taskfile.csv', 'r') as file:
            lines = file.readlines()  # Read all lines
            print(lines[0])  # Print the header
            for line in lines[1:]:
                print(line)  # Print each task
    except Exception as e:
        print(f"Error viewing tasks: {e}")

def main():
    opentaskfile()  # Ensure the task file exists
    file_path = 'taskfile.csv'
    lines = load_tasks_from_file(file_path)  # Load existing tasks

    while True:
        print("============ To-Do List ============")
        print("1. Add New Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            # Add a new task
            title = input("Enter the title of the task to add: ")
            description = input("Enter the description: ")
            category = input("Enter the category: ")
            add_task(title, description, category)  # Code to add a task

        elif choice == '2':
            # View all tasks
            view_task()  # Code to display tasks

        elif choice == '3':
            # Mark a task as completed
            mark_task_completed(file_path)  # Code to mark a task as completed

        elif choice == '4':
            # Delete a task
            title = input("Enter the title of the task to delete: ")
            delete_task(title)
        elif choice == '5':
            # Exit the program
            save_tasks_to_file(file_path, lines)  # Save tasks before exiting
            print("Exiting the program")
            break

        else:
            print("Invalid choice. Please enter a valid choice.")

if __name__ == "__main__":
    main()  # Start the program
