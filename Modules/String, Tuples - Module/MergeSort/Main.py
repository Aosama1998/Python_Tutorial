def merge_sort_iterative(arr):
    n = len(arr)
    current_size = 1

    # Merge subarrays of size `current_size`
    while current_size < n:
        # Traverse all subarrays of `current_size`
        for left in range(0, n, 2 * current_size):
            # Calculate mid and right indices of the subarray
            mid = min(left + current_size, n)
            right = min(left + 2 * current_size, n)

            # Merge subarrays [left:mid] and [mid:right]
            merge(arr, left, mid, right)

        # Double the size of the subarray
        current_size *= 2

def merge(arr, left, mid, right):
    # Create temporary arrays for merging
    left_part = arr[left:mid]
    right_part = arr[mid:right]

    i = j = 0
    k = left

    # Merge the temporary arrays back into the original array
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    # Copy remaining elements from left_part
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    # Copy remaining elements from right_part
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

# Test
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort_iterative(arr)
print(arr)
