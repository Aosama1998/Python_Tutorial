numbers = [55 , 23, 546, 893, 170, 30 , 45 , 53, 78]


for i in range(1 , len(numbers)):

    j = i

    while numbers[j-1] > numbers[j] and j >0:

        numbers[j-1] , numbers[j] = numbers[j] , numbers[j-1] # Swapping method that can be used in python

        j-=1



print(numbers)