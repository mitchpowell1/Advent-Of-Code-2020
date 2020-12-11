from itertools import product
from copy import deepcopy
from enum import Enum


class SeatState(Enum):
    Occupied = '#'
    Floor = '.'
    Empty = 'L'


def count_occupancy(seat_grid):
    return sum(row.count(SeatState.Occupied) for row in seat_grid)


def compute_occupancy(seat_grid, occ_tolerance=4, scan_seats=False):
    next_state = deepcopy(seat_grid)
    changed = False
    for row in range(len(seat_grid)):
        for col in range(len(seat_grid[row])):
            current_state = seat_grid[row][col]
            occ_count = 0
            for rd, cd in product([-1, 0, 1], repeat=2):
                if rd == cd == 0:
                    continue
                scale_factor = 1
                while True:
                    rd, cd = (rd * scale_factor, cd * scale_factor)
                    checked_row = row + rd
                    checked_col = col + cd

                    valid_row = len(seat_grid) > checked_row >= 0
                    valid_col = len(seat_grid[row]) > checked_col >= 0
                    if not valid_row or not valid_col or seat_grid[checked_row][checked_col] == SeatState.Empty:
                        break

                    if seat_grid[checked_row][checked_col] == SeatState.Occupied:
                        occ_count += 1
                        break

                    if not scan_seats:
                        break

                    scale_factor += 1

            if current_state == SeatState.Empty and occ_count == 0:
                changed = True
                current_state = SeatState.Occupied

            elif current_state == SeatState.Occupied and occ_count >= occ_tolerance:
                changed = True
                current_state = SeatState.Empty

            next_state[row][col] = current_state
    return next_state, changed


def part_one(seats):
    layout = seats
    while True:
        layout, changed = compute_occupancy(layout, 4, False)
        if not changed:
            break
    return count_occupancy(layout)


def part_two(seats):
    layout = seats
    while True:
        layout, changed = compute_occupancy(layout, 5, True)
        if not changed:
            break
    return count_occupancy(layout)


def main():
    with open('input.txt', 'r') as f:
        rows = [[SeatState(char) for char in line.strip()] for line in f]

    print(part_one(rows))
    print(part_two(rows))


main()