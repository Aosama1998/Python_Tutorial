import os

# Function to add a task to the list
def add_task(task_list, task):
    task_list.append(task)
    print(f"Task '{task}' added successfully.")

# Function to remove a completed task
def remove_task(task_list, task):
    if task in task_list:
        task_list.remove(task)
        print(f"Task '{task}' removed successfully.")
    else:
        print(f"Task '{task}' not found in the list.")

# Function to view the current task list
def view_tasks(task_list):
    if not task_list:
        print("The task list is empty.")
    else:
        print("Current Tasks:")
        for idx, task in enumerate(task_list, start=1):
            print(f"{idx}. {task}")

# Function to save tasks to a file
def save_tasks(task_list, filename):
    try:
        with open(filename, 'w') as file:
            for task in task_list:
                file.write(task + '\n')
        print(f"Tasks saved to '{filename}'.")
    except Exception as e:
        print(f"Error saving tasks: {e}")

# Function to load tasks from a file
def load_tasks(filename):
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                tasks = [line.strip() for line in file]
            print(f"Tasks loaded from '{filename}'.")
            return tasks
        else:
            print(f"File '{filename}' not found. Starting with an empty task list.")
            return []
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return []

# Main function to manage the task list
def main():
    task_list = []
    filename = "tasks.txt"
    
    # Load existing tasks from file
    task_list = load_tasks(filename)
    
    while True:
        print("\nTask Manager Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Save Tasks")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            view_tasks(task_list)
        elif choice == '2':
            task = input("Enter the task to add: ").strip()
            if task:
                add_task(task_list, task)
            else:
                print("Task cannot be empty.")
        elif choice == '3':
            task = input("Enter the task to remove: ").strip()
            remove_task(task_list, task)
        elif choice == '4':
            save_tasks(task_list, filename)
        elif choice == '5':
            print("Exiting Task Manager. Goodbye!")
            save_tasks(task_list, filename)  # Save before exiting
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
