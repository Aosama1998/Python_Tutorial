
# Taking input from the user
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Performing operations
sum_result = first_number + second_number
subtraction_result = first_number - second_number
multiplication_result = first_number * second_number
division_result = first_number / second_number if second_number != 0 else "Undefined (division by zero)"

# Printing the results
print("Sum: ", sum_result)
print("Subtraction: ", subtraction_result)
print("Multiplication: ", multiplication_result)
print("Division: ", division_result)
