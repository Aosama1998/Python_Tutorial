numbers = [55 , 23, 546, 893, 170, 30 , 45 , 53, 78]

size = len(numbers)

for i in range(size):
    
    swapped = False

    for j in range(0 , size-1-i):

        if numbers[j] > numbers[j+1]:
        
            temp = numbers[j+1]
            numbers[j+1] = numbers[j]
            numbers[j] = temp
            swapped = True

    if not swapped:
        break

print(numbers)

