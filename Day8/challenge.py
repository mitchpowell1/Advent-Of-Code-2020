def make_instruction(line):
    instruction, increment = line.split(' ')
    return [instruction, int(increment)]


def part_one(instructions):
    accumulator = 0
    i = 0
    visited = set()
    while i < len(instructions):
        if i in visited:
            return accumulator, True
        visited.add(i)
        instruction = instructions[i]

        if instruction[0] == 'jmp':
            i += instruction[1]
            continue

        if instruction[0] == 'acc':
            accumulator += instruction[1]

        i += 1
    return accumulator, False


def part_two(instructions):
    for instruction in instructions:
        if instruction[0] == 'acc':
            continue

        replacement = 'nop' if instruction[0] == 'jmp' else 'jmp'

        tmp = instruction[0]
        instruction[0] = replacement
        result, looped = part_one(instructions)
        if not looped:
            return result
        instruction[0] = tmp


def main():
    with open('input.txt', 'r') as f:
        instructions = [make_instruction(line.strip()) for line in f]

    print(part_one(instructions)[0])
    print(part_two(instructions))


if __name__ == '__main__':
    main()
