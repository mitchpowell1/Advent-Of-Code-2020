from math import radians, e


def rotate(direction, degrees, value):
    if direction == 'R':
        degrees = -1 * degrees
    new_o = value * (e ** (radians(degrees) * 1j))

    return round(new_o.real) + round(new_o.imag) * 1j


def apply_direction(direction, dist, value):
    if direction == 'N':
        return value + dist * 1j
    if direction == 'S':
        return value - dist * 1j
    if direction == 'E':
        return value + dist
    if direction == 'W':
        return value - dist


def get_distance(value):
    return int(abs(value.real) + abs(value.imag))


def part_one(instructions):
    orientation = 1 + 0j
    ship = 0 + 0j

    for action, value in instructions:
        if action in 'RL':
            orientation = rotate(action, value, orientation)

        elif action == 'F':
            ship += value * orientation

        else:
            ship = apply_direction(action, value, ship)

    return get_distance(ship)


def part_two(instructions):
    waypoint = 10 + 1j
    ship = 0 + 0j

    for action, value in instructions:
        if action in 'RL':
            waypoint = rotate(action, value, waypoint)

        elif action == 'F':
            ship += value * waypoint

        else:
            waypoint = apply_direction(action, value, waypoint)

    return get_distance(ship)


with open('input.txt', 'r') as f:
    directions = [(line[0], int(line[1:])) for line in f]

print(part_one(directions))
print(part_two(directions))

