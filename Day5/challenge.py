def get_seat_id(line):
    converted = ''.join(['0' if char in 'FL' else '1' for char in line])
    return int(converted, 2)


def main():
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file]

    seat_ids = sorted([get_seat_id(line) for line in lines])
    missing_seat = -1

    for i in range(len(seat_ids) - 1):
        expected = seat_ids[i] + 1
        if seat_ids[i + 1] != expected:
            missing_seat = expected
            break

    print('C1: {}'.format(seat_ids[-1]))
    print('C2: {}'.format(missing_seat))


if __name__ == '__main__':
    main()
