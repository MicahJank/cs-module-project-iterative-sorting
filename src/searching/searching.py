def linear_search(arr, target):
    i = 0
    while i <= len(arr) - 1:
        if arr[i] == target:
            return i
        
        i += 1

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    midpoint = int((len(arr) - 1) / 2)
    # sliced_arr = arr.copy()
    # current_item = sliced_arr[midpoint]
    # i = 0

    print("array", arr)
    while arr[midpoint] != target:
        if target > arr[midpoint]:
            end = len(arr) - 1
            midpoint = int((len(arr[midpoint:end]) - 1) / 2)
            print("midpoint greater", midpoint)
        elif target < arr[midpoint]:
            end = midpoint
            midpoint = int((len(arr[:end]) - 1) / 2)
            print("midpoint lesser", midpoint)

    else:
        print(midpoint)
        return midpoint
            
    # print(sliced_arr[midpoint])
    # while current_item != target:
    #     if target > current_item:
    #         sliced_arr = sliced_arr[midpoint:len(sliced_arr)-1]
    #         print("greater than", sliced_arr)
    #     elif target < current_item:
    #         sliced_arr = sliced_arr[0:midpoint]
    #         print("less than", sliced_arr)

    #     midpoint = int((len(sliced_arr)-1) / 2)
    #     current_item = sliced_arr[midpoint]
    #     print("current item end", current_item)
    #     print("midpoint end", midpoint)
    # else:
    #     return midpoint

    return -1  # not found
