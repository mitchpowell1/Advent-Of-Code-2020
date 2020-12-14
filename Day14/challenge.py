import re

value_regex = re.compile(r'mem\[(?P<mem_address>\d+)\] = (?P<mem_value>\d+)')
mask_regex = re.compile(r'mask = (?P<mask_value>[X01]+)')


def modify_bit(n, p, b):
    mask = 1 << p
    return (n & ~mask) | ((b << p) & mask)


def part_one(instructions):
    memory = {}
    mask = 'X' * 36
    for instruction in instructions:
        if match := mask_regex.match(instruction):
            mask = match.group('mask_value')
            continue
        if match := value_regex.match(instruction):
            address = int(match.group('mem_address'))
            value = int(match.group('mem_value'))
            for i in range(35, -1, -1):
                if mask[i] == 'X':
                    continue
                new_bit = int(mask[i])
                value = modify_bit(value, 35 - i, new_bit)
            memory[address] = value
    return sum(v for v in memory.values())


def get_masks(mask):
    masks = [mask]
    finalized_masks = []

    while len(masks) > 0:
        mask = masks.pop()
        first_floating_bit = mask.find('X')
        if first_floating_bit == -1:
            finalized_masks.append(mask)
            continue
        for bit in '01':
            masks.append(mask[0:first_floating_bit] + bit + mask[first_floating_bit + 1:])

    return finalized_masks


def part_two(instructions):
    memory = {}
    mask = 'X' * 36
    all_masks = []
    for instruction in instructions:
        if match := mask_regex.match(instruction):
            mask = match.group('mask_value')
            all_masks = get_masks(mask)
        if match := value_regex.match(instruction):
            address = int(match.group('mem_address'))
            value = int(match.group('mem_value'))
            for parsed_mask in all_masks:
                new_address = address
                for i in range(35, -1, -1):
                    if mask[i] != '0':
                        new_address = modify_bit(new_address, 35 - i, int(parsed_mask[i]))
                memory[new_address] = value

    return sum(v for v in memory.values())


def main():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f]

    print(part_one(lines))
    print(part_two(lines))
    return


if __name__ == '__main__':
    main()
