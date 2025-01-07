num = int (input("Please enter your number "))


result = 1
while num:

    if num <= 1:
        break
    
    result *= num
    num -=1

print(result)