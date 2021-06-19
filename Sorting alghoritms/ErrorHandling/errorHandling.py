from Generator.numbersGenerator import generator


def users_choice(choice):
    if choice == "Gen":
        numbers = type_gen()
    elif choice == "Own":
        numbers = own_numbers()
    else:
        print("Wrong input, please write it again")
        numbers = users_choice(input())
    return numbers


def own_numbers():
    print("Please, write your numbers: ")
    try:
        numbers = [int(x) for x in input().split()]
    except ValueError:
        print("Wrong data entered, please try again")
        numbers = own_numbers()
    return numbers


def type_gen():
    print(
        "Please, write a type of numbers ('A' - a-shape numbers, 'V' - v-shape numbers, 'I' - increasing numbers,"
        "'D' - decreasing numbers or 'R' - random numbers): ")
    num_type = check_num_type(input())
    print("Please, write the amount of numbers: ")
    amount = check_amount(input())
    numbers = generator(amount, num_type)
    return numbers


def check_num_type(num_type):
    num_types = ["A", "V", "I", "D", "R"]
    if num_type in num_types:
        return num_type
    else:
        print("Wrong data entered, please try again")
        print(
            "Please, write a type of numbers ('A' - a-shape numbers, 'V' - v-shape numbers, 'I' - increasing numbers,"
            "'D' - decreasing numbers or 'R' - random numbers): ")
        return check_num_type(input())


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
