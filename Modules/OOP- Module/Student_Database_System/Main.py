class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []  # List to store grades

    def add_grade(self, grade):
        """Add a grade to the student's list of grades."""
        if 0 <= grade <= 100:  # Valid grades are between 0 and 100
            self.grades.append(grade)
        else:
            print("Invalid grade! Please enter a grade between 0 and 100.")

    def calculate_average(self):
        """Calculate and return the average of the grades."""
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0  # Return 0 if there are no grades

    def display_info(self):
        """Display the student's information and grades."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.calculate_average():.2f}")


class StudentDatabase:
    def __init__(self):
        self.students = []  # List to store student objects

    def add_student(self, name, age):
        """Add a new student to the database."""
        student = Student(name, age)
        self.students.append(student)
        print(f"Student {name} added successfully!")

    def list_students(self):
        """List all students in the database."""
        if not self.students:
            print("No students in the database.")
            return
        for idx, student in enumerate(self.students, start=1):
            print(f"{idx}. {student.name} (Age: {student.age})")

    def get_student_by_name(self, name):
        """Retrieve a student object by name."""
        for student in self.students:
            if student.name == name:
                return student
        print(f"No student found with the name '{name}'.")
        return None


# Example Scenario
def main():
    database = StudentDatabase()

    # Adding new students
    database.add_student("Alice", 20)
    database.add_student("Bob", 22)

    # Adding grades to Alice
    alice = database.get_student_by_name("Alice")
    if alice:
        alice.add_grade(85)
        alice.add_grade(90)
        alice.add_grade(78)

    # Adding grades to Bob
    bob = database.get_student_by_name("Bob")
    if bob:
        bob.add_grade(88)
        bob.add_grade(76)
        bob.add_grade(92)

    # Display all students
    print("\nStudent List:")
    database.list_students()

    # Display individual student information
    print("\nStudent Information:")
    if alice:
        alice.display_info()
    if bob:
        bob.display_info()


if __name__ == "__main__":
    main()
