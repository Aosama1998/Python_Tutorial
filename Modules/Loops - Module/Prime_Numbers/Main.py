# Input from the user
num = int(input("Please enter a number: "))

# Check if the number is less than or equal to 1
if num <= 1:
    print("This is not a prime number.")
else:
    for n in range(2, num + 1):  # Loop through numbers from 2 to 'num'
        prime = True  # Assume the number is prime

        # We check if 'n' is divisible by any number from 2 to n-1
        for i in range(2, n):  
            if n % i == 0:  # If 'n' is divisible by any 'i', it's not prime
                prime = False
                break  # Exit the loop early since we know it's not prime
        
        if prime:
            print(f"{n} is a prime number.")
