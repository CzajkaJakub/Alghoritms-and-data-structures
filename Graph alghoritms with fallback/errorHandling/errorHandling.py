def check_type_of_input(type):
    types = ['O', 'F']
    if type in types:
        return type
    else:
        print("Wrong data entered, please try again:")
        return check_type_of_input(input())


def task_type(type):
    try:
        amount = int(type)
        if amount > 0 and amount < 5:
            return amount
        else:
            print("Wrong data entered, please try again:")
            return task_type(input())
    except(ValueError):
        print("Wrong data entered, please try again:")
        return task_type(input())
