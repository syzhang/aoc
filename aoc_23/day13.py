"""
day 13
"""

from utils import get_input
import numpy as np


def loop_through(patterns, smudge=1):
    """loop through patterns"""
    h = 0
    v = 0
    for p in patterns:
        grid = p.split("\n")
        # get rid of empty lines
        grid = [x for x in grid if x]
        # convert grid to numpy array of 1s and 0s
        grid = np.array([[1 if x == "#" else 0 for x in line] for line in grid])
        h += total_h(grid, smudge)
        v += total_h(grid.transpose(), smudge)
    print(f"total: {h * 100 + v}")


def diff_h(grid, i):
    """diff horizontal"""
    dist = min(i, grid.shape[0] - i)
    return sum(
        grid[i + j, k] != grid[i - j - 1, k]
        for k in range(grid.shape[1])
        for j in range(dist)
    )


def total_h(grid, smudge=1):
    """total horizontal"""
    return sum(i for i in range(grid.shape[0]) if diff_h(grid, i) == smudge)


# main
if __name__ == "__main__":
    # get input
    day = 13
    # data = get_input(day, test_data=True)
    data = get_input(day, test_data=False)

    # part a
    patterns = data.split("\n\n")
    # loop_through(patterns, smudge=0)

    # part b
    loop_through(patterns, smudge=1)
