import random


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
    print("Please, write the amount of numbers: ")
    amount = check_amount(input())
    numbers = [random.randint(1, 10 * amount) for x in range(amount)]
    return numbers


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


def check_type(type):
    types = ['BST', 'AVL']
    try:
        if type in types:
            return type
        else:
            print("Wrong data entered, please try again:")
            return check_type(input())
    except ValueError:
        print("Wrong data entered, please try again:")
        return check_type(input())


def check_command(command):
    commands = ['Stop', 'Continue']
    try:
        if command in commands:
            return command
        else:
            print("Wrong data entered, please try again:")
            return check_command(input())
    except ValueError:
        print("Wrong data entered, please try again:")
        return check_command(input())


def check_task(task):
    tasks = [1, 2, 3, 4, 5, 6, 7]
    try:
        task = int(task)
        if task in tasks:
            return task
        else:
            print("Wrong data entered, please try again:")
            return check_task(input())
    except ValueError:
        print("Wrong data entered, please try again:")
        return check_task(input())


