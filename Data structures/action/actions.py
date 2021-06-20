import time


lentree = 0
isa = 0


class TreeNode(object):
    def __init__(self, val):
        global lentree
        lentree += 1
        self.val = val
        self.left = None
        self.right = None


class BST_Tree(object):
    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left,
                                    key)
        else:
            root.right = self.insert(root.right,
                                     key)
        return root


def bst(numbers):
    myTree = BST_Tree()
    root = None
    for i in numbers:
        root = myTree.insert(root, i)
    return root


def avl(numbers):
    numbers = new_numbers(sorted(numbers), [])
    return bst(numbers)


def new_numbers(numbers, new):
    if not numbers:
        return
    median = len(numbers) // 2
    new.append(numbers[median])
    new_numbers(numbers[:median], new)
    new_numbers(numbers[median + 1:], new)
    return new


def action(task, tree):
    global lentree
    global isa

    if task == 1:
        low(tree, [])
        hight(tree, [])
        return tree


    elif task == 2:
        print("How many elements would you like to delete?")
        x = check_amount(input())
        if x > lentree:
            print("Too many elements, please try again")
            action(2, tree)
        else:
            i = 0
            while i < x:
                print('Enter the key')
                key = check_amount(input())
                check_tree(tree, key)
                if isa == 1:
                    isa = 0
                    tree = delete_element(tree, key)
                    lentree -= 1
                    i += 1
                else:
                    print('Wrong data entered, please try again')
        return tree


    elif task == 3:
        start = time.time_ns()
        print(lentree)
        arr = inorder(tree, [], lentree)
        end = time.time_ns()
        print("Sorting time {} ns".format(end - start))
        print(arr)
        return tree


    elif task == 4:
        start = time.time_ns()
        arr = preorder(tree, [], lentree)
        end = time.time_ns()
        print("Sorting time {} ns".format(end - start))
        print(arr)
        return tree



    elif task == 5:
        return postorder(tree)


    elif task == 6:
        print("Enter a key")
        key = check_amount(input())
        check_tree(tree, key)
        if isa == 1:
            isa = 0
            preorder2(tree, [], lentree, key)
        else:
            print('Wrong data entered, please try again')
            action(6, tree)
        return tree


    elif task == 7:
        return balanceTheTree(tree)


def low(root, arr):
    if root:
        arr.append(root.val)
        low(root.left, arr)
    else:
        print("The way to the lowest element : ", arr)


def hight(root, arr):
    if root:
        arr.append(root.val)
        hight(root.right, arr)
    else:
        print("The way to the biggest element : ", arr)


def inorder(root, arr, n):
    if root:
        inorder(root.left, arr, n)
        arr.append(root.val)
        inorder(root.right, arr, n)
    if len(arr) == n:
        return arr


def preorder(root, arr, n):
    if root:
        arr.append(root.val)
        preorder(root.left, arr, n)
        preorder(root.right, arr, n)
    if n == len(arr):
        return arr


def count(tree):
    w = 1
    if tree:
        w += count(tree.right)
        w += count(tree.left)
        return w
    else:
        return 0


def preorder2(root, arr, n, key):
    if root:
        if root.val == key:
            w = count(root)
            print(preorder(root, [], w))
            return
        elif root.val < key:
            preorder2(root.right, arr, n, key)
        else:
            preorder2(root.left, arr, n, key)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)
        del root


def delete_element(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = delete_element(root.left, key)

    elif key > root.val:
        root.right = delete_element(root.right, key)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = getTheSuc(root.right)
        root.val = temp.val
        root.right = delete_element(root.right, temp.val)
    return root


def getTheSuc(root):
    current = root
    while current.left is not None:
        current = current.left
    return current


def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def isBalanced(root):
    if root is None:
        return 'true'
    lh = height(root.left)
    rh = height(root.right)
    if abs(lh - rh) <= 1:
        tmp = isBalanced(root.left)
        if tmp == 'true':
            tmp2 = isBalanced(root.right)
            return tmp2
        else:
            return tmp
    return root.val


def check_tree(tree, key):
    global isa
    if tree:
        if tree.val == key:
            isa = 1
            return
        else:
            check_tree(tree.left, key)
            check_tree(tree.right, key)


def balanceTheTree(tree):
    global lentree
    tmp = isBalanced(tree)
    if tmp == 'true':
        print("Balancing process is over")
    else:
        tree = delete_element(tree, tmp)
        newTree = BST_Tree()
        tree = newTree.insert(tree, tmp)
        lentree -= 1
        tree = balanceTheTree(tree)
    return tree
