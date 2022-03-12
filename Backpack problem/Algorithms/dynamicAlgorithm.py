def dynamic_algo(number_of_items, size_of_bag, items):
    matrix = [[0 for j in range(size_of_bag+1)] for i in range(number_of_items + 1)]
    elements = []
    maxi = 0
    size = 0
    for i in range(1, number_of_items+1):
        for j in range(1, size_of_bag+1):
            if items[i-1][0] > j:
                matrix[i][j] = matrix[i-1][j]
            else:
                x1 = matrix[i - 1][j]
                x2 = matrix[i - 1][j - items[i - 1][0]] + items[i - 1][1]
                matrix[i][j] = max(x1, x2)
                if matrix[i][j] > maxi:
                    maxi = matrix[i][j]
                    size = j


    print("A matrix of the dynamic programming algorithm")
    for i in matrix:
        print(i)

    x = size_of_bag
    for i in range(number_of_items):
        if matrix[number_of_items-i][x] > matrix[number_of_items-1-i][x]:
            elements.append(number_of_items-i)
            x -= items[number_of_items-i-1][0]


    print("A maximal value of a contents of the bag is {}. \nA size of the bag is {}."
          " \nThe bag should content elements: {}.".format(maxi, size, elements))
    return