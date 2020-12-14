import math


def part_one(arrival, bus_ids):
    normalized_ids = [int(id) for id in bus_ids if id != 'x']
    min_wait = math.inf
    min_wait_id = 0

    for bus_id in normalized_ids:
        loops = math.ceil(arrival / bus_id)
        wait = (bus_id * loops) - arrival
        if wait < min_wait:
            min_wait = wait
            min_wait_id = bus_id

    return min_wait_id * min_wait


def part_two_brute_force(bus_ids):
    i = 100000000000000
    while True:
        j = i
        condition_met = True
        for bus_id in bus_ids:
            j += 1
            if bus_id == 'x':
                continue
            bus_id = int(bus_id)
            if j % bus_id != 0:
                condition_met = False
                break
        if condition_met:
            break

        i += 1
    return i + 1


def p2_better(bus_ids):
    buses = [1 if b == 'x' else int(b) for b in bus_ids]
    time = 0
    p = 1
    for bus in buses:
        while time % int(bus) != 0:
            time += p
        p *= bus
        time += 1
    return time - len(buses)


def main():
    with open('input.txt', 'r') as f:
        arrival = int(f.readline())
        bus_ids = f.readline().split(',')

    print(part_one(arrival, bus_ids))
    print(p2_better(bus_ids))


if __name__ == '__main__':
    main()
