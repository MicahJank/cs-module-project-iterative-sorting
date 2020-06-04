def linear_search(arr, target):
    i = 0
    while i <= len(arr) - 1:
        if arr[i] == target:
            return i
        
        i += 1

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # midpoint = int((len(arr) - 1) / 2)
    start = 0
    end = len(arr) - 1
    mid = int((start + end) / 2)

    if len(arr):        
        while arr[mid] != target:
            print(start, mid, end)
            if arr[mid] > target:
                end = mid
            elif arr[mid] < target:
                start = mid
            mid = int((start + end) / 2) 
        else:
            return mid

    return -1  # not found
