import time

swaps = 0
comparison = 0


def pre_shell_sort(numbers_to_sort):
    start = time.time_ns()
    sorted_numbers, comparison, swaps = shell_sort_knuth(numbers_to_sort)
    end = time.time_ns()
    print("Sorted numbers : {}\nSorting time in ns.: {}\nComparison: {}\nNumber of swaps: {}".format(sorted_numbers,
                                                                                                     (end - start),
                                                                                                     comparison, swaps))
    return


def shell_sort_knuth(numbers_to_sort):
    global swaps
    global comparison
    n = 1
    k = 1
    while n < len(numbers_to_sort) / 3:
        n = (3 ** k - 1) // 2
        k += 1
    k -= 1
    while n > 0:
        print(n)
        for i in range(n):
            numbers_to_sort = bubble_sort(numbers_to_sort, n)
        k -= 1
        n = (3 ** k - 1) // 2
    return numbers_to_sort, comparison, swaps


def bubble_sort(arr, step):
    global swaps
    global comparison
    n = len(arr)
    for i in range(n):
        for j in range(n - i - step):
            comparison += 1
            if arr[j] < arr[j + step]:
                swaps += 1
                arr[j], arr[j + step] = arr[j + step], arr[j]
    return arr
