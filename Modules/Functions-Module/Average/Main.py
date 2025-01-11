arr = [38, 27, 43, 3, 9, 82, 10]



def average(arr):

    if len(arr) == 0:
        raise ValueError("The list is empty. Cannot calculate average.")
    
    # Calculate the sum of the list
    total_sum = sum(arr)
    
    # Calculate the average
    average = total_sum / len(arr)
    
    return average


print(average(arr))
