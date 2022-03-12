import sys
from ErrorHandling.errorHandling import *
from TestFileGenerator.testFileGen import generator
from Algorithms.dynamicAlgorithm import dynamic_algo
from Algorithms.greedyAlgorithm import zach_algo
from Algorithms.forceAlgorithm import *


def main():
    print("Choose type of input 'F' if random generated data from file or 'O' if own: ")
    input_type = check_type_of_input(input())
    if input_type == 'F':
        generator()
    number_of_items, size_of_bag, items = data(input_type)
    action(number_of_items, size_of_bag, items)
    return


def action(number_of_items, size_of_bag, items):
    print(
        "Choose a type of algorithm:\nDynamic programming algorithm - 'AD'\nGreedy algorithm - 'AZ'\nBrute force algorithm -'AB'")
    type_of_algo = check_type_of_algo(input())
    pick_algo(number_of_items, size_of_bag, items, type_of_algo)
    return 0


def pick_algo(number_of_items, size_of_bag, items, type_of_algo):
    if type_of_algo == 'AD':
        dynamic_algo(number_of_items, size_of_bag, items)
    elif type_of_algo == 'AZ':
        print("Choose type of sorting by value: 'I' - increasing or 'D' - decreasing")
        type_AZ = check_type(input())
        zach_algo(number_of_items, size_of_bag, items, type_AZ)
    elif type_of_algo == 'AB':
        force_algo(number_of_items, size_of_bag, items)
    else:
        print("Something went wrong, check the code")
    return 0


if __name__ == '__main__':
    main()
