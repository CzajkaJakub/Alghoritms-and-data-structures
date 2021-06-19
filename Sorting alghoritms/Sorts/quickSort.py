import time

swaps = 0
comparison = 0


def pre_quick_sort(numbers_to_sort):
    start = time.time_ns()
    sorted_numbers, comparison, swaps = quick_sort(numbers_to_sort, 0, len(numbers_to_sort) - 1)
    end = time.time_ns()
    print("Sorted numbers : {}\nSorting time in ns.: {}\nComparison: {}\nNumber of swaps: {}".format(sorted_numbers,
                                                                                                     (end - start),
                                                                                                     comparison, swaps))
    return


def quick_sort(numbers_to_sort, start, end):
    global swaps
    global comparison
    if len(numbers_to_sort) == 1:
        return numbers_to_sort
    if start < end:
        pivot = numbers_to_sort[end]
        print("Pivot: {}".format(pivot))
        j = start
        for i in range(start, end):
            comparison += 1
            if numbers_to_sort[i] >= pivot:
                numbers_to_sort[i], numbers_to_sort[j] = numbers_to_sort[j], numbers_to_sort[i]
                swaps += 1
                j += 1
        numbers_to_sort[end], numbers_to_sort[j] = numbers_to_sort[j], numbers_to_sort[end]
        swaps += 1
        quick_sort(numbers_to_sort, start, j - 1)
        quick_sort(numbers_to_sort, j + 1, end)

        return numbers_to_sort, comparison, swaps
