def get_nth_num(starting_numbers, n=2020):
    spoken = {num: i + 1 for (i, num) in enumerate(starting_numbers)}

    num = 0
    for i in range(len(starting_numbers) + 2, n + 1):
        if num in spoken:
            next_num = (i - 1) - spoken[num]
            spoken[num] = i - 1
            num = next_num
        else:
            spoken[num] = i - 1
            num = 0
    return num


def main():
    with open('input.txt', 'r') as f:
        starting_numbers = [int(n) for n in f.readline().split(',')]

    print(get_nth_num(starting_numbers))
    print(get_nth_num(starting_numbers, 30000000))

    return


if __name__ == '__main__':
    main()
