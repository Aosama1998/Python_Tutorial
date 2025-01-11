
def factorial(n):

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    elif n == 0 or n ==1:
        return 1
    
    else:
        return n * factorial(n-1)


    

def main():

    num = input("Please Enter your number : ")

    print(factorial(int(num)))


main()