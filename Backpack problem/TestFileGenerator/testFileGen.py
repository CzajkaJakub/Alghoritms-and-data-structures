import random


def generator():
    amount_of_elements = 234
    size_of_backpack = 9678
    file = open("TestFileGenerator/test.txt", "w")
    wiersz = "{} {}\n".format(amount_of_elements, size_of_backpack)
    file.write(wiersz)

    for i in range(amount_of_elements):
        size_of_item = random.randint(1, amount_of_elements // 2)
        value_of_item = random.randint(1, amount_of_elements // 2)
        wiersz = "{} {}\n".format(size_of_item, value_of_item)
        file.write(wiersz)
