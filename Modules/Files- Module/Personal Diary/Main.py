import os
from datetime import datetime

# Function to create a new diary entry
def create_entry(filename):
    try:
        # Open the diary file in append mode to add new entries
        with open(filename, 'a') as file:
            print("Write your diary entry (press Enter and then type 'exit' to finish):")
            entry = []
            
            # Allow users to write multiple lines
            while True:
                line = input()
                if line.lower() == 'exit':
                    break
                entry.append(line)
            
            # Optionally add timestamp
            timestamp = input("Would you like to add a timestamp to this entry? (yes/no): ").strip().lower()
            if timestamp == 'yes':
                entry.insert(0, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
            # Write the entry to the file
            file.write("\n".join(entry) + "\n\n")
            print("Your diary entry has been saved successfully.")
    
    except PermissionError:
        print("Error: Permission denied. You do not have permission to write to this file.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to view previous diary entries
def view_entries(filename):
    try:
        if not os.path.exists(filename):
            print("Diary file does not exist.")
            return
        
        with open(filename, 'r') as file:
            entries = file.read()
            if entries:
                print("\nPrevious Diary Entries:")
                print(entries)
            else:
                print("No entries in the diary yet.")
    
    except PermissionError:
        print("Error: Permission denied. You do not have permission to read from this file.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to handle user input and menu selection
def main():
    filename = "diary.txt"  # Define the file where the diary entries will be saved
    
    while True:
        print("\nPersonal Diary Application")
        print("1. Create a new diary entry")
        print("2. View previous diary entries")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ").strip()
        
        if choice == '1':
            create_entry(filename)
        elif choice == '2':
            view_entries(filename)
        elif choice == '3':
            print("Exiting the Diary application. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
