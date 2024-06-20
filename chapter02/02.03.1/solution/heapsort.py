#!/usr/bin/python2


def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

def heapify(array):
    """ Build heap """
    # Middle in array
    start = (len(array) - 2) / 2
    while start >= 0:
        perc_down(array, start, len(array) - 1)
        start -= 1

def perc_down(array, start, end):
    """ Check/modify heap structure """
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

