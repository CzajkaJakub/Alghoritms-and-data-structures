import time

swaps = 0
comparison = 0


def pre_heap_sort(numbers_to_sort):
    start = time.time_ns()
    sorted_numbers, comparison, swaps = heap_sort(numbers_to_sort)
    end = time.time_ns()
    print("Sorted numbers : {}\nSorting time in ns.: {}\nComparison: {}\nNumber of swaps: {}".format(sorted_numbers,
                                                                                                     (end - start),
                                                                                                     comparison, swaps))
    return


def heap_sort(numbers_to_sort):
    global swaps
    global comparison
    n = len(numbers_to_sort)
    for i in range(n // 2 - 1, -1, -1):
        heapify(numbers_to_sort, n, i)
    for i in range(n - 1, -1, -1):
        numbers_to_sort[i], numbers_to_sort[0] = numbers_to_sort[0], numbers_to_sort[i]
        heapify(numbers_to_sort, i, 0)
    return numbers_to_sort, comparison, swaps


def heapify(numbers_to_sort, n, i):
    global swaps
    global comparison
    small = i
    left = 2 * i + 1
    right = 2 * i + 2
    comparison += 2
    if left < n and numbers_to_sort[small] > numbers_to_sort[left]:
        small = left
    if right < n and numbers_to_sort[small] > numbers_to_sort[right]:
        small = right
    if small != i:
        numbers_to_sort[i], numbers_to_sort[small] = numbers_to_sort[small], numbers_to_sort[i]
        swaps += 1
        heapify(numbers_to_sort, n, small)
