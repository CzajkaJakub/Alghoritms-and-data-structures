def check_type_of_input(type):
    types = ['O', 'F']
    if type in types:
        return type
    else:
        print("Wrong data entered, please try again:")
        return check_type_of_input(input())


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
    types = ['Adj', 'Graph']
    if type in types:
        return type
    else:
        print("Wrong data entered, please try again:")
        return check_type(input())


def check_task(task):
    tasks = ['DFS', 'DEL']
    if task in tasks:
        return task
    else:
        print("Wrong data entered, please try again:")
        return check_task(input())
