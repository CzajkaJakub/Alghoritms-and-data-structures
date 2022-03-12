import sys


def zach_algo(number_of_items, size_of_bag, items, type_az):
    value_of_back = 0
    size_of_back = 0
    numbers = []
    values = []
    sizes = []

    for i in range(number_of_items):
        siz, val = items[i]
        sizes.append(siz)
        values.append(val)

    if type_az == "D":
        index = values.index(max(values))
        while (size_of_back + sizes[index]) <= size_of_bag:
            numbers.append(index)
            value_of_back += values[index]
            size_of_back += sizes[index]
            values[index] = 0
            sizes[index] = 0
            index = values.index(max(values))
        print(
            "A value of a contents of the bag is {}. \nA size of the bag is {}. \nThe bag contentS elements: {}".format(
                value_of_back, size_of_back, numbers))
    elif type_az == "I":
        index = values.index(min(values))
        while (size_of_back + sizes[index]) <= size_of_bag:
            numbers.append(index)
            value_of_back += values[index]
            size_of_back += sizes[index]
            values[index] = 999999
            sizes[index] = 999999
            index = values.index(min(values))
        print(
            "A value of a contents of the bag is {}. \nA size of the bag is {}. \nThe bag contents elements: {}".format(
                value_of_back, size_of_back, numbers))
    else:
        print("Something went wrong")
        sys.exit(0)
    return
