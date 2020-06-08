def linear_search(arr, target):
    i = 0
    while i <= len(arr) - 1:
        if arr[i] == target:
            return i
        
        i += 1

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    mid = int((start + end) / 2)

    # first check to see if there is anything inside of the array, if there isnt we dont need to do a search
    if len(arr):
        # the loop will keep comparing he value in the middle of the array to see if it matches the target
        while arr[mid] != target:
            # if the target is smaller we need to search the lower half of the array - therefore we can reset the end value to the mid
            if arr[mid] > target:
                end = mid
            # if the target is bigger we do the opposite since we want to check the upper half of the array now
            elif arr[mid] < target:
                start = mid
            
            # every iteration of the loop we reset the mid point since we are searching a new part of the array
            mid = int((start + end) / 2) 
        else:
            return mid

    return -1  # not found
