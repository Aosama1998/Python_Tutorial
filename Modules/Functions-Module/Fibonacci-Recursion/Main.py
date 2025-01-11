

def Fibonnaci(num):

    if num < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    
    if num == 0:
        return [0]
    
    if num == 1:
        return [0,1]
    
    result = Fibonnaci(num - 1)

    result.append(result[-1] + result[-2])

    return result



num = int(input("Please Enter your number"))       


result = Fibonnaci(num)

print(f"The Fibonnaci sequence for your number {num} is {result}")