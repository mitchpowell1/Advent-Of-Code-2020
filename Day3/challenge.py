from functools import reduce

TREE_INDICATOR = '#'


def compute_tree_collisions(tree_grid, slope):
    row = 0
    col = 0
    map_width = len(tree_grid[0])
    encountered_trees = 0

    while row < len(tree_grid):
        if tree_grid[row][col] == TREE_INDICATOR:
            encountered_trees += 1
        row += slope[0]
        col = (col + slope[1]) % map_width
    return encountered_trees


def main():
    with open('input.txt', 'r') as file:
        tree_grid = [line.strip() for line in file]

    challenge_1_result = compute_tree_collisions(tree_grid, (1, 3))
    challenge_2_slopes = [
        (1, 1),
        (1, 3),
        (1, 5),
        (1, 7),
        (2, 1)
    ]
    challenge_2_operands = [compute_tree_collisions(tree_grid, slope) for slope in challenge_2_slopes]
    challenge_2_result = reduce(lambda a, b: a*b, challenge_2_operands)

    print('Challenge 1 result: {}'.format(challenge_1_result))
    print('Challenge 2 result: {}'.format(challenge_2_result))


if __name__ == '__main__':
    main()
