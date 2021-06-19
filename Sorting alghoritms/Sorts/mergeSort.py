import time


def pre_merge_sort(numbers_to_sort):
    start = time.time_ns()
    sorted_numbers = merge_sort(numbers_to_sort)
    end = time.time_ns()
    print("Sorted numbers : {}\nSorting time in ns.: {}".format(sorted_numbers, (end - start)))
    return


def merge_sort(numbers_to_sort):
    if len(numbers_to_sort) > 1:
        x = len(numbers_to_sort) // 2

        left = numbers_to_sort[:x]
        right = numbers_to_sort[x:]

        merge_sort(left)
        merge_sort(right)

        pos_left = pos_right = pos_numbers = 0

        while pos_left < len(left) and pos_right < len(right):
            if left[pos_left] > right[pos_right]:
                numbers_to_sort[pos_numbers] = left[pos_left]
                pos_left += 1
            else:
                numbers_to_sort[pos_numbers] = right[pos_right]
                pos_right += 1
            pos_numbers += 1

        while pos_left < len(left):
            numbers_to_sort[pos_numbers] = left[pos_left]
            pos_left += 1
            pos_numbers += 1

        while pos_right < len(right):
            numbers_to_sort[pos_numbers] = right[pos_right]
            pos_right += 1
            pos_numbers += 1

        return numbers_to_sort
