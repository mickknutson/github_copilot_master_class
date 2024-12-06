#!/usr/bin/python2


def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

def heapify(array):
    # Middle in array
    start = (len(array) - 2) / 2
    while start >= 0:
        perc_down(array, start, len(array) - 1)
        start -= 1

def perc_down(array, start, end):
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

def partition(array, low, high):
    i = low - 1
    pivot = array[high]
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            swap(array, i, j)
    swap(array, i+1, high)
    return i+1

def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi-1)
        quicksort(array, pi+1, high)

def sort(array):
    n = len(array)
    quicksort(array, 0, n-1)




if __name__ == "__main__":
    array = [17, 9, 13, 8, 7, -5, 6, 11, 3, 4, 1, 2]
    sort(array)
    print(array)

