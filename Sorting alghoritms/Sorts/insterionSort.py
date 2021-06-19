import time


def pre_insertion_sort(numbers_to_sort):
    start = time.time_ns()
    sorted_numbers, comparison, swaps = insertion_sort(numbers_to_sort)
    end = time.time_ns()
    print("Sorted numbers : {}\nSorting time in ns.: {}\nComparison: {}\nNumber of swaps: {}".format(sorted_numbers,
                                                                                                     (end - start),
                                                                                                     comparison, swaps))
    return


def insertion_sort(numbers_to_sort):
    comparison = 0
    swaps = 0
    for i in range(1, len(numbers_to_sort)):
        key = numbers_to_sort[i]
        j = i - 1
        comparison += 1
        while j >= 0 and key > numbers_to_sort[j]:
            numbers_to_sort[j + 1] = numbers_to_sort[j]
            swaps += 1
            j -= 1
            comparison += 1
        numbers_to_sort[j + 1] = key
        swaps += 1
    return numbers_to_sort, comparison, swaps
