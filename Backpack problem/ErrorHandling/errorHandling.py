import sys


def check_type_of_input(type_of_input):
    types = ['O', 'F']
    if type_of_input in types:
        return type_of_input
    else:
        print("Wrong data entered, please try again:")
        return check_type_of_input(input())


def data(inp_type):
    if inp_type == "O":
        return read_own()
    else:
        return read_file()


def read_file():
    try:
        file = open("TestFileGenerator/test.txt", "r")
        number_of_items, size_of_bag = (int(x) for x in file.readline().split(" "))
        if number_of_items < 0 or size_of_bag < 0:
            print("There is an error in the file.")
            sys.exit(0)
        else:
            items = {}
            for i in range(number_of_items):
                size, val = [int(i) for i in file.readline().split(" ")]
                if size < 0 or val < 0:
                    print("There is an error in the file.")
                    sys.exit(0)
                else:
                    items[i] = (size, val)
            return number_of_items, size_of_bag, items
    except ValueError:
        print("There is an error in the file.")
        sys.exit(0)
    except TypeError:
        print("There is an error in the file.")
        sys.exit(0)


def read_own():
    number_of_items = check_amount(input("Input the number of items:"))
    size_of_bag = check_amount(input("Input the size of a bag:"))
    items = {}
    for _ in range(number_of_items):
        print("Input a size and a value of the item:")
        size, val = check_item()
        items[_] = (size, val)
    return number_of_items, size_of_bag, items


def check_amount(amount):
    try:
        amount = int(amount)
        if amount > 0:
            return amount
        else:
            print("Wrong data entered, please try again:")
            return check_amount(input())
    except ValueError:
        print("Wrong data entered, please try again:")
        return check_amount(input())


def check_item():
    try:
        size, val = [int(x) for x in input().split()]
        if size > 0 and val > 0:
            return size, val
        else:
            print("Wrong data entered, please try again:")
            return check_item()
    except ValueError:
        print("Wrong data entered, please try again:")
        return check_item()


def check_type(type_az):
    types = ["I", "D"]
    if type_az in types:
        return type_az
    else:
        print("Wrong data, try again")
        return check_type(input())


def check_type_of_algo(type_of_algo):
    types = ["AD", "AZ", "AB"]
    if type_of_algo in types:
        return type_of_algo
    else:
        print("Wrong data entered, please try again")
        return check_type_of_algo(input())
