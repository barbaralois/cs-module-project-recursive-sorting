# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # create variables to keep track of our place in each list
    a_index = 0
    b_index = 0

    for item in range(len(merged_arr)):
        # if we're at the end of A
        if a_index > len(arrA) - 1:
            # set the current number to b_index
            merged_arr[item] = arrB[b_index]
            # increment
            b_index += 1

        # if we're at the end of B
        elif b_index > len(arrB) - 1:
            # set the current number to a_index
            merged_arr[item] = arrA[a_index]
            # increment
            a_index += 1

        # we're not at the end of either list yet
        else:
            # if value A is larger than value B
            if arrA[a_index] > arrB[b_index]:
                # set the current number to B (the smaller)
                merged_arr[item] = arrB[b_index]
                # increment B
                b_index += 1
            # if value B is larger than value A
            else:
                # set the current number to A (the smaller)
                merged_arr[item] = arrA[a_index]
                # increment A
                a_index += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # find the middle value
    middle = len(arr) // 2
    # left is all items to the left of that
    left = arr[:middle]
    # right is all items to the right of that
    right = arr[middle:]

    # if there's more than 1 number left...
    if len(left) > 1:        
        # run merge_sort again, finding a new middle & so on
        left = merge_sort(left)
    # if there's more than 1 number left...
    if len(right) > 1:
        # run merge_sort again, finding a new middle & so on
        right = merge_sort(right)
    
    # combine the sorted lists using the helper function above
    arr = merge(left, right)


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

