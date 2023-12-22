"""
day 21
"""
from collections import defaultdict
from utils import get_input


def parse_grid(input):
    """parse input"""
    grid = []
    for line in input.split("\n"):
        if not line:
            continue
        grid.append(list(line))

    # find S in grid
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == "S":
                start = (i, j)
                break
    return grid, start


def part_a(grid, visited, steps=6):
    """part a"""
    # recursive for new starts
    all_visited = set()
    for _ in range(steps):
        step_visited = set()
        for v in visited:
            tmp = recursive(grid, v)
            step_visited.update(tmp)
        visited = step_visited
        all_visited.update(visited)
    return len(visited)


def recursive(grid, start):
    """recursive"""
    # possible moves
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # record all positions visited
    new_locs = set()
    # start at S
    current = start
    # check all possible moves, if . or S, move there
    for m in moves:
        # check if in grid
        if (
            current[0] + m[0] < 0
            or current[0] + m[0] >= len(grid)
            or current[1] + m[1] < 0
            or current[1] + m[1] >= len(grid[0])
        ):
            continue
        if (
            grid[current[0] + m[0]][current[1] + m[1]] == "."
            or grid[current[0] + m[0]][current[1] + m[1]] == "S"
        ):
            next = (current[0] + m[0], current[1] + m[1])
            new_locs.add(next)
    return new_locs


# main
if __name__ == "__main__":
    # get input
    # input = get_input(day=21, test_data=True)
    input = get_input(day=21, test_data=False)

    # part a
    grid, start = parse_grid(input)
    # total = part_a(grid, [start], steps=64)
    # print(total)

    # part b
