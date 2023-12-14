"""
day 14
"""

from utils import get_input


def tilt(grid, direction="north"):
    """tilt towards east (right of row)"""
    # transform grid
    if direction == "north":
        grid = transpose(grid, clockwise=True)
    # move all O in a column to the top, skipping #
    tilted = tuple(
        "#".join(["".join(sorted(p)) for p in row.split("#")]) for row in grid
    )
    # transform back
    if direction == "north":
        tilted = transpose(tilted, clockwise=False)
        # upside down
        tilted = tilted[::-1]
    return tilted


def make_grid(data):
    """make grid from data"""
    grid = data.split("\n")
    # get rid of empty lines
    grid = [x for x in grid if x]
    return tuple(grid)


def spin(grid):
    """spin grid 4 times"""
    for _ in range(4):
        grid = transpose(grid, clockwise=True)
        grid = tuple(
            "#".join(["".join(sorted(p)) for p in row.split("#")]) for row in grid
        )
    return grid


def transpose(grid, clockwise=False):
    """transpose grid anti-clockwise, reverse=True for clockwise"""
    if clockwise:
        return tuple("".join(row) for row in zip(*grid[::-1]))
    else:
        return tuple("".join(row) for row in zip(*grid))


def count_rock(grid):
    """count rock in row"""
    counts = 0
    for i, row in enumerate(grid[::-1]):
        counts += (i + 1) * row.count("O")
    print(counts)


def find_cycle(grid):
    """find cycle"""
    # find cycle
    spins = 0
    cache = {}
    cycle_length = None
    while True:
        grid = spin(grid)
        if not cycle_length:
            if grid in cache:
                cycle_start = spins
                cycle_length = spins - cache[grid]
                break
            else:
                cache[grid] = spins
        spins += 1
    return cycle_start, cycle_length, cache


# main
if __name__ == "__main__":
    # get input
    day = 14
    # data = get_input(day, test_data=True)
    data = get_input(day, test_data=False)

    # part a
    grid = make_grid(data)
    # tilted_grid = tilt(grid, direction='north')
    # print(tilted_grid)
    # count_rock(tilted_grid)

    # part b
    cycle_start, cycle_length, cache = find_cycle(grid)
    spins = 1000000000
    offset = cycle_start - cycle_length
    idx = (spins - 1 - offset) % cycle_length + offset
    for k, v in cache.items():
        if v == idx:
            count_rock(k)
