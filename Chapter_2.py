from time import perf_counter
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


# Merge sort
def merge(array, p, q, r):
    left_index = q - p + 1
    right_index = r - q

    # left = 0:left_index-1 && right = 0:right_index-1
    left = [None] * left_index-1
    right = [None] * right_index-1

    for i in range(0, left_index-1):
        left[i] = array[p + i]

    for j in range(0, right_index-1):
        right[j] = array[q + j + 1]

    i = 0       # left's smallest remaining element
    j = 0       # right's smallest remaining element
    k = p       # location to fill in array

    # while each array left, right contains an unmerged element
    # copy the smallest unmerged element back inot array[p:r]

    while i < left_index and j < right_index:
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1

        else:
            array[k] = right[j]
            j += 1

        k += 1

    # after traversing left, right entirely, copy remainder
    # of the other to the end of array[p:r]

    while i < left_index:
        array[k] = left[i]
        i += 1
        k += 1

    while j < right_index:
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


    



array = [5, 2, 4, 6, 1, 3]

print(array)

start_time = perf_counter()
insertion_sort(array, len(array))
end_time = perf_counter()

print("after sorting:")
print(f"time taken: {end_time - start_time}")
print(array)