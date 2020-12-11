def part_one(adapters):
    one_count = 0
    three_count = 0
    for i in range(1, len(adapters)):
        if adapters[i] - adapters[i - 1] == 1:
            one_count += 1
        elif adapters[i] - adapters[i - 1] == 3:
            three_count += 1

    return (one_count + 1) * (three_count + 1)


def part_two(adapters):
    memo = [1 if v <= 3 else 0 for v in adapters]

    for i in range(len(adapters)):
        memo[i] += sum(
            memo[j]
            for j in range(max(0, i - 3), i)
            if adapters[i] - adapters[j] <= 3
        )

    return memo[-1]


def part_two_space_optimized(adapters):
    memo = [0, 0, 0, 0]

    for i in range(len(adapters)):
        memo[i % 4] = sum(
            memo[j % 4]
            for j in range(max(0, i - 3), i)
            if adapters[i] - adapters[j] <= 3
        )
        if adapters[i] <= 3:
            memo[i % 4] += 1

    return max(memo)


def main():
    with open('input.txt', 'r') as f:
        lines = sorted([int(line) for line in f])
    print(part_one(lines))
    print(part_two(lines))
    print(part_two_space_optimized(lines))

    return


if __name__ == '__main__':
    main()
