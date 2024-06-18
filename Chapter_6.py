import math

# Max-Heap Property: 
# Array[parent(i)] >= Array[i]

# Min-Heap Property: 
# Array[parent(i)] <= Array[i]

class Max_Heap:
    heapsize = 0

    def __init__(self, heapsize):
        self = [0 for i in range(heapsize)]

    def parent(i): 
        return i // 2
    
    def left(i): 
        return 2 * i
    
    def right(i):
        return 2 * i + 1
    

    # checks index i of max_heap self to see if it violates the max heap property
    # runs in O(lg(n))
    def max_heapify(self, i):
        left = left(i)
        right = right(i)

        if left <= self.heapsize and self[left] > self[right]:
            largest = left

        else: largest = i

        if right <= self.heapsize and self[right] > self[largest]:
            largest = right

        if largest != i:
            swap(self, i, largest)
            self.max_heapify(self, largest)
            

    # runs max_heapify on half the array, ensuring that the array is sorted. 
    # O(n), which calls an O(lg(n)) func, so running time = O(nlg(n))
    def build_max_heap(self, n):
        self.heapsize = n
        for i in range((n // 2), 1, -1):
            self.max_heapify(self, i)

    # goes through the entire array, swapping the top of the heap with the 
    # botton & runs max_heapify() to compare each node & make sure no child
    # node is greater than the parent, essentially swapping it.
    # build_max_heap() := O(n) & max_heapify() := O(lg(n)), therefore
    # heapsort := O(nlg(n))
    def heapsort(self, n):
        self.build_max_heap(self, n)
        for i in range(n, 2, -1):
            swap(self, 1, i)
            self.heapsize = self.heapsize - 1
            self.max_heapify(self, 1)
        

    def insert():

    def extract_max():

    def increase_key():


    def peek_max():



def swap(array, x, y):
    temp = array[x]
    array[x] = array[y]
    array[y] = temp