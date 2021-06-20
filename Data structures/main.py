from action.actions import *
from action.errorsHand.error import *


def main():
    print("Write: 'Gen' if you would like to choose generator's numbers or"
          " 'Own' if you you would like to pick own numbers")
    numbers = users_choice(input())
    print("Your numbers: {}".format(numbers))
    print("Write: 'BST' if you would like to create a classic Binary Searching Tree or "
          "'AVL' if you you would like to create a self-balancing Binary Search Tree")
    type = check_type(input())
    tree = tree_choice(type, numbers)
    program_status(tree)
    return 0


def tree_choice(choice, numbers):
    if choice == 'AVL':
        tree = avl(numbers)
        return tree
    elif choice == 'BST':
        tree = bst(numbers)
        return tree


def program_status(data):
    while True:
        tree = task(data)
        print("Write: 'Stop' if you would like to finish program or 'Continue' otherwise.")
        command = check_command(input())
        if command == 'Stop':
            break


def task(tree):
    print("Please, choose a task: \n "
          "1 - Road to the highest and the lowest value\n "
          "2 - Delete element (enter keys) \n "
          "3 - In-order \n "
          "4 - Pre-order \n "
          "5 - Postorder with deleting \n "
          "6 - Subtree (enter a key) \n "
          "7 - Balancing tree")
    task = check_task(input())
    return action(task, tree)








if __name__ == "__main__":
    main()
