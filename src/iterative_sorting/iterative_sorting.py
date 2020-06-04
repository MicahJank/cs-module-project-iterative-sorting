# TO-DO: Complete the selection_sort() function below 
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

        # Store the items i want to swap in variables
        current = arr[cur_index]
        smallest = arr[smallest_index]
        # and then swap them out with eachother
        arr[smallest_index] = current
        arr[cur_index] = smallest

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # swapped variable is used to check when the loop has swapped any items around
    # if swapped remains false through the entire loop it means the array must be sorted
    swapped = False
    for i in range(0, len(arr) - 1):
        # store the current item and next item so i can swap them later
        current_item = arr[i]
        next_item = arr[i+1]

        # check to see if the next item in the list is higher, if it is we should swap the elements
        if next_item < current_item:
            arr[i] = next_item
            arr[i+1] = current_item
            swapped = True
    
    # if swapped is true that means there was a value in the array that needed to be swapped around which means we dont know the array is sorted yet
    # in that case i use recursion and called the bubble sort method again passing in the arr - this will go through the loop again
    if swapped:
        bubble_sort(arr)

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
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
