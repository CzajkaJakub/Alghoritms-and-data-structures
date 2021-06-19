import random


def generator(amount, num_type):
    if num_type == "A":
        numbers_a_shape = sorted([random.randint(1, 10 * amount) for x in range(amount // 2)]) + sorted(
            [random.randint(1, 10 * amount) for x in range(amount // 2)])[::-1]
        return numbers_a_shape

    elif num_type == "V":
        numbers_v_shape = sorted([random.randint(1, 10 * amount) for x in range(amount // 2)])[::-1] + sorted(
            [random.randint(1, 10 * amount) for x in range(amount // 2)])
        return numbers_v_shape

    elif num_type == "I":
        increasing_numbers = sorted([random.randint(1, 10 * amount) for x in range(amount)])
        return increasing_numbers

    elif num_type == "D":
        decreasing_numbers = sorted([random.randint(1, 10 * amount) for x in range(amount)])[::-1]
        return decreasing_numbers

    elif num_type == "R":
        random_numbers = [random.randint(1, 10 * amount) for x in range(amount)]
        return random_numbers
