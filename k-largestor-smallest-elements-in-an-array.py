""" Find the k largest(or smallest) elements in an array | Added Min Heap method """
import heapq as hq


def first_k_elements_heap(arr, k):
    """O(n) time operation"""
    size = len(arr)
    min_heap = []

    for i in range(k):
        min_heap.append(arr[i])
    hq.heapify(min_heap)

    for i in range(k, size):
        if min_heap[0] > arr[i]:
            continue
        else:
            min_heap[0] = min_heap[-1]
            min_heap.pop()
            min_heap.append(arr[i])
            hq.heapify(min_heap)

    for i in min_heap:
        print(i, end=" ")


arr = [11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45]
k = 3
first_k_elements_heap(arr, k)


def k_largest(arr, k):
    """Sort the given array arr in reverse order. O(nk)"""
    arr.sort(reverse=True)
    for i in range(k):
        print(arr[i], end=" ")


arr = [1, 23, 12, 9, 30, 2, 50]

k = 3
k_largest(arr, k)
