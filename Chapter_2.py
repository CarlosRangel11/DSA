from time import perf_counter
import numpy as np
import math

# addressing the sorting problem

# reorder <a_1, a_2, a_3, ... > 
# such that a_1 <= a_2 <= a_3 <= ...

# Insertion sort
def insertion_sort(array, n):
    for i in range(1, n):
        key = array[i]

        # insert array[i] into sorted subarray
        j = i - 1
        while (j >= 0 and array[j] > key):
            array[j+1] = array[j]
            j = j - 1

        array[j+1] = key

# Bubble sort
def bubble_sort(array, n):
    for i in range(0, n):
        for j in range(n-1, i, -1):
            if array[j] < array[j-1]:
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp


# Merge sort
# array: a passed array (duh)
# p: leftmost index
# q: mid index
# r: rightmost index
def merge(array, p, q, r):

    # print(f"Working on subarray with params:\narray: {array}\n\tp = {p}, q = {q}, r = {r}")
    # sleep(3)

    left_length = q - p + 1
    right_length = r - q

    # left = 0:left_length-1 && right = 0:right_length-1
    left = np.empty(left_length, dtype=int)
    right = np.empty(right_length, dtype=int)

    # copy left half of array
    for i in range(0, left_length):
        left[i] = array[p + i]

    # copy right half of array
    for j in range(0, right_length):
        right[j] = array[q + 1 + j]

    i = 0       # left's smallest remaining element
    j = 0       # right's smallest remaining element
    k = p       # location to fill in array

    # while each array left, right contains an unmerged element
    # copy the smallest unmerged element back inot array[p:r]

    while i < left_length and j < right_length:
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1

        else:
            array[k] = right[j]
            j += 1

        k += 1

    # after traversing left, right entirely, copy remainder
    # of the other to the end of array[p:r]
    while i < left_length:
        array[k] = left[i]
        i += 1
        k += 1

    while j < right_length:
        array[k] = right[j]
        j += 1
        k += 1

def merge_sort(array, p, r):
    if p >= r:
        return
    q = math.floor((p+r)/2)
    merge_sort(array, p, q)
    merge_sort(array, q+1, r)

    merge(array, p, q, r)


    



array = np.random.randint(99, size=(10000))

copy_of_array = array.copy()
print(f"""
##############################################################
Insertion sort on array of length: {len(copy_of_array)}
""")
#print(f"{copy_of_array}\n")


start_time = perf_counter()
insertion_sort(copy_of_array, len(copy_of_array))
end_time = perf_counter()

#print(f"after sorting:\n{copy_of_array}\n")

print(f"time taken: {end_time - start_time : .6f}")



copy_of_array = array.copy()
print(f"""
##############################################################
Bubble sort on array of length: {len(copy_of_array)}
""")
#print(f"{copy_of_array}\n")


start_time = perf_counter()
bubble_sort(copy_of_array, len(copy_of_array))
end_time = perf_counter()

#print(f"after sorting:\n{copy_of_array}\n")

print(f"time taken: {end_time - start_time : .6f}")



copy_of_array = array.copy()
print(f"""
##############################################################
Merge sort on array of length: {len(copy_of_array)}
""")
#print(f"{copy_of_array}\n")

start_time = perf_counter()
merge_sort(copy_of_array, 0, len(copy_of_array)-1)
end_time = perf_counter()

#print(f"after sorting:\n{copy_of_array}\n")

print(f"time taken: {end_time - start_time : .6f}")