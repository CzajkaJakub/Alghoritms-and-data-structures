from ErrorHandling.errorHandling import users_choice
import Sorts.shellSort
import Sorts.heapSort
import Sorts.insterionSort
import Sorts.mergeSort
import Sorts.quickSort


def main():
    programStatus = 1
    while programStatus:
        print(
            "Write: 'Gen' if you would like to choose generator's numbers or 'Own' "
            "if you you would like to pick own numbers")
        numbers = users_choice(input())
        print("Your numbers: {}".format(numbers))
        sort_type(numbers)
        print("If you want to quit program, type 'Q': ")
        programStatus = quitProgram(input())
    return 0


def quitProgram(choice):
    if choice == 'Q' or choice == 'q':
        return 0
    else:
        return 1


def sort_type(numbers_to_sort):
    types = ["Insertion", "Merge", "Heap", "Shell", "Quick"]
    print("Please, pick one sorting type : {}".format(types))
    users_sort_type_choice = input()
    if users_sort_type_choice in types:
        pick_sort(users_sort_type_choice, numbers_to_sort)
    else:
        print("Wrong data entered, please try again")
        sort_type(numbers_to_sort)
    return


def pick_sort(users_sort_type_choice, numbers_to_sort):
    if users_sort_type_choice == "Insertion":
        Sorts.insterionSort.pre_insertion_sort(numbers_to_sort)
    elif users_sort_type_choice == "Merge":
        Sorts.mergeSort.pre_merge_sort(numbers_to_sort)
    elif users_sort_type_choice == "Heap":
        Sorts.heapSort.pre_heap_sort(numbers_to_sort)
    elif users_sort_type_choice == "Shell":
        Sorts.shellSort.pre_shell_sort(numbers_to_sort)
    elif users_sort_type_choice == "Quick":
        Sorts.quickSort.pre_quick_sort(numbers_to_sort)
    return


if __name__ == "__main__":
    main()
