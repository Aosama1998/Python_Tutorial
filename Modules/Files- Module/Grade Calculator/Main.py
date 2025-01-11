import os

def input_grades():
    """Input grades from the user and handle exceptions for invalid input."""
    grades = []
    print("Enter grades for each subject (type 'done' to finish):")
    while True:
        try:
            user_input = input("Enter grade: ").strip()
            if user_input.lower() == "done":
                break
            grade = float(user_input)
            if grade < 0 or grade > 100:
                print("Grade must be between 0 and 100. Try again.")
                continue
            grades.append(grade)
        except ValueError:
            print("Invalid input! Please enter a numeric grade or type 'done' to finish.")
    return grades

def calculate_average(grades):
    """Calculate and return the average of the grades."""
    if not grades:
        print("No grades entered to calculate an average.")
        return None
    return sum(grades) / len(grades)

def save_grades_to_file(grades, filename="grades.txt"):
    """Save the grades to a file."""
    try:
        with open(filename, "w") as file:
            file.write("\n".join(map(str, grades)))
        print(f"Grades saved to '{filename}'.")
    except (OSError, IOError) as e:
        print(f"Error saving grades to file: {e}")

def load_grades_from_file(filename="grades.txt"):
    """Load grades from a file if it exists."""
    if not os.path.exists(filename):
        print(f"No previous grades found in '{filename}'. Starting fresh.")
        return []
    try:
        with open(filename, "r") as file:
            grades = [float(line.strip()) for line in file.readlines()]
        print(f"Grades loaded from '{filename}'.")
        return grades
    except (ValueError, OSError, IOError) as e:
        print(f"Error reading grades from file: {e}")
        return []

def main():
    grades = load_grades_from_file()
    print("\nPreviously stored grades:", grades)

    new_grades = input_grades()
    grades.extend(new_grades)

    average = calculate_average(grades)
    if average is not None:
        print(f"\nAverage grade: {average:.2f}")

    save_grades_to_file(grades)

if __name__ == "__main__":
    main()
