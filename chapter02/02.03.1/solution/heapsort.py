#!/usr/bin/python2


def swap(array, i, j):
    """
    Swaps the elements at positions i and j in the given array.

    Parameters:
    array (list): The input array.
    i (int): The index of the first element to swap.
    j (int): The index of the second element to swap.
    """
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

def heapify(array):
    """
    Rearranges the elements in the array to form a max heap.
    Parameters:
    array (list): The array to be heapified.
    Returns:
    None
    """
    
    # Middle in array
    start = (len(array) - 2) / 2
    while start >= 0:
        perc_down(array, start, len(array) - 1)
        start -= 1

def perc_down(array, start, end):
    """
    Perform a downward percolate operation on a binary heap.
    Args:
        array (list): The array representing the binary heap.
        start (int): The index of the element to percolate down from.
        end (int): The index of the last element in the heap.
    Returns:
        None
    """
    
    largest = 2 * start + 1
    while largest <= end:
        # left child < right child
        if (largest < end) and (array[largest] < array[largest + 1]):
            largest += 1
        # biggest child > parent
        if (array[largest] > array[start]):
            swap(array, largest, start)
            start = largest
            largest = 2 * start + 1
        else: 
            return

def sort(array):
    """
    Sorts the given array in ascending order using the Heap Sort algorithm.

    Parameters:
    array (list): The list of elements to be sorted.

    Returns:
    None: The function modifies the original array in-place.
    """
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                swap(array, j, j+1)
        end -= 1




if __name__ == "__main__":
    array = [17, 9, 13, 8, 7, -5, 6, 11, 3, 4, 1, 2]
    sort(array)
    print(array)

