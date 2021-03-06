# TO-DO: Complete the selection_sort() function below 
# time complexity - O(n^2)
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # loop through the array again this time start the loop 1 ahead of i - this will check everything on the right of
        # the current index
        for j in range(i + 1, len(arr)):
            # compare the array at position j with whatever is the current smallest item in the array
            # if array at position j is smaller than we can update the smallest index
            if arr[j] < arr[smallest_index]:
                smallest_index = j

    # # Store the items i want to swap in variables
        # current = arr[cur_index]
        # smallest = arr[smallest_index]
    # # and then swap them out with eachother
        # arr[smallest_index] = current
        # arr[cur_index] = smallest

        # better way
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
# time complexity - O(n^2)
def bubble_sort(arr):

    made_a_swap = True
    while made_a_swap:
        made_a_swap = False

        for i in range(len(arr) - 1):
            j = i + 1

            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                made_a_swap = True

    # # swapped variable is used to check when the loop has swapped any items around
    # # if swapped remains false through the entire loop it means the array must be sorted
    # swapped = False
    # for i in range(0, len(arr) - 1):
    #     # store the current item and next item so i can swap them later
    #     current_item = arr[i]
    #     next_item = arr[i+1]

    #     # check to see if the next item in the list is higher, if it is we should swap the elements
    #     if next_item < current_item:
    #         arr[i] = next_item
    #         arr[i+1] = current_item
    #         swapped = True
    
    # # if swapped is true that means there was a value in the array that needed to be swapped around which means we dont know the array is sorted yet
    # # in that case i use recursion and called the bubble sort method again passing in the arr - this will go through the loop again
    # if swapped:
    #     bubble_sort(arr)

    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
# original time complexity - O(n^2)
def count_sort(arr, maximum=None):
    if len(arr) == 0:
        return arr

    if maximum == None:
        maximum = max(arr)

    counts = [0] * (maximum + 1)

    for value in arr:
        if value < 0:
            return "Error, negative numbers not allowed in Count Sort"
        counts[value] += 1

    for i in range(len(counts)):
        while counts[j] = i
            j += 1
            counts[i] -= 1
            
    # # first check to see if the arr is empty or not, if it is i just return the empty array
    # if len(arr) == 0:
    #     return arr

    # # next i check if maximum is none - if it is i find the max value in the arr and that becomes the maximum
    # if maximum is None:
    #     maximum = max(arr)

    
    # # buckets will store a list of 0's
    # buckets = [0 for _ in range(maximum+1)]

    # # loop through arr
    # for item in arr:
    #     # if there are any negative numbers in the arr we will return the error string
    #     if item < 0:
    #         return "Error, negative numbers not allowed in Count Sort"
    #     # if no error then we increase the buckets by 1 at the index that represents the current item in arr
    #     buckets[item] += 1
    
    # i = 0
    # # loop
    # for item in range(maximum+1):
    #     # loop again up to the current item index
    #     for _ in range(buckets[item]):
    #         # 
    #         arr[i] = item
    #         i += 1

    return arr
