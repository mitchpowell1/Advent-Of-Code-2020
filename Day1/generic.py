from functools import reduce


def find_tuple(data, number_of_elements, desired_sum):
    # Precomputing dataset minimum helps to avoid unnecessary iterations
    data_min = min(data)

    def find_tuple_helper(tuple_size, tuple_sum):
        if tuple_size == 1:
            if tuple_sum in data:
                return tuple_sum,
            return -1

        for datum in data:
            remainder = tuple_sum - datum
            # Don't continue if the result couldn't possibly contain this datum
            if remainder < data_min:
                continue
            result = find_tuple_helper(tuple_size - 1, remainder)
            if result != -1 and datum not in result:
                return (datum,) + result
        return -1

    return find_tuple_helper(number_of_elements, desired_sum)


def get_tuple_product(tup):
    return reduce(lambda a, b: a*b, tup)


def main():
    input_numbers = set([int(line) for line in open('input.txt', 'r')])
    desired_sum = 2020

    result1 = find_tuple(input_numbers, 2, desired_sum)
    result2 = find_tuple(input_numbers, 3, desired_sum)
    print(result1)
    print(get_tuple_product(result1))
    print()
    print(result2)
    print(get_tuple_product(result2))


if __name__ == "__main__":
    main()
