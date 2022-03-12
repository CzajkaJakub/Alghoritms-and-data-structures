def force_algo(number_of_items, size_of_bag, items):
    bits = binary(number_of_items)
    maxi = 0
    numbers_of_items = []
    for i in bits:
        val = 0
        size = 0
        for j in range(len(i)):
            if i[j] == 1:
                temp_size, temp_val = items[j]
                val += temp_val
                size += temp_size
        if size <= size_of_bag and val > maxi:
            maxi = val
            numbers_of_items = i
    print(
        "A maximal value of a contents of the bag is {}. \nA size of the bag is {}. \nThe bag should content elements: {}".format(
            maxi, size_of_bag, numbers_of_items))
    return


def binary(number_of_items):
    bits = []
    for i in range(1, 2 ** number_of_items):
        bit = []
        for _ in range(number_of_items):
            bit.append(0)
        num = i
        pos = 0
        while num >= 1:
            if (num % 2) == 1:
                bit[pos] = 1
            num //= 2
            pos += 1
        bits.append(bit)
    return bits
