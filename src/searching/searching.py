# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # start is longer than the array? item wasn't found
    if start > end:
        return -1
    # if we're not at the end yet...    
    else:
        # find the middle value
        middle = start + end // 2
        # that number is the guess
        guess = arr[middle]
        # compare to target, if they match
        if guess == target:
            # return middle (aka the index of that num)
            return middle
        # compare to target, if target is larger...
        elif target > guess:
            # recursively call function on items above the mid
            return binary_search(arr, target, (middle+1), end)
        # compare to target, if target is smaller...
        else:
            # recursively call function on items below the mid
            return binary_search(arr, target, start, (middle-1))


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

