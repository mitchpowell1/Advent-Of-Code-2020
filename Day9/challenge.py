def part_one(numbers, preamble_size=25):
    for i in range(preamble_size, len(numbers)):
        preamble_set = set(numbers[i - preamble_size: i])
        found = False
        for number in preamble_set:
            required = numbers[i] - number
            if required == number:
                continue
            elif required in preamble_set:
                found = True
                break
        if not found:
            return numbers[i]


def part_two_brute_force(numbers, sum_value):
    window_size = 2
    while window_size < len(numbers):
        for i in range(len(numbers) - window_size):
            numbers_slice = numbers[i: i + window_size]
            window_sum = sum(numbers_slice)
            if window_sum == sum_value:
                return min(numbers_slice) + max(numbers_slice)
        window_size += 1


def part_two_optimized(numbers, sum_value):
    memo = [
        [n for n in numbers],
        [0 for _ in numbers]
    ]

    window_size = 2
    while window_size < len(numbers):
        for i in range(len(numbers) - window_size):
            window_sum = memo[window_size % 2][i - 1] + numbers[i]
            if window_sum == sum_value:
                numbers_slice = numbers[i - (window_size - 1):i+1]
                return min(numbers_slice) + max(numbers_slice)
            memo[(window_size - 1) % 2][i] = window_sum
        window_size += 1

    return -1


def main():
    with open('input.txt', 'r') as f:
        lines = [int(line) for line in f]
    part_one_sol = part_one(lines)
    part_two_sol = part_two_optimized(lines, part_one_sol)

    print(part_one_sol)
    print(part_two_sol)


if __name__ == '__main__':
    main()
