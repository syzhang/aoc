"""
day 11
"""
from utils import get_input
from collections import deque


def read_universe(data):
    """read universe"""
    old_universe = data.strip().split()
    # find #s
    galaxies = find_galaxies(old_universe)
    return old_universe, galaxies


def find_galaxies(universe):
    """find galaxies"""
    # find #s
    galaxies = [
        (r, c)
        for r in range(len(universe))
        for c in range(len(universe[0]))
        if universe[r][c] == "#"
    ]
    return galaxies


def expand_universe(data):
    """expand universe"""
    old_universe, galaxies = read_universe(data)
    # rows and columns without #
    rows, cols = find_empty_rc(old_universe, galaxies)
    # expand universe
    new_universe = duplicate_rows_cols(old_universe, list(rows), list(cols))
    # squish universe
    new_universe = ["".join(row) for row in new_universe]
    return new_universe


def find_empty_rc(old_universe, galaxies):
    """find empty row and column"""
    # find empty row and column
    rows = set([r for r in range(len(old_universe))]) - set([r for r, _ in galaxies])
    cols = set([c for c in range(len(old_universe[0]))]) - set([c for _, c in galaxies])
    return rows, cols


def expand_empty_rc(old_universe, galaxies, n=1e6):
    """expand empty row and column"""
    dim_x = len(old_universe[0])
    dim_y = len(old_universe)
    expand_n = n - 1
    # expansion X
    x = 0
    while x < dim_x:
        if not any(o[0] == x for o in galaxies):
            dim_x += expand_n
            for i, val in enumerate(galaxies):
                if val[0] > x:
                    galaxies[i] = (val[0] + expand_n, val[1])
            x += expand_n
        x += 1

    # expansion y
    y = 0
    while y < dim_y:
        if not any(o[1] == y for o in galaxies):
            dim_y += expand_n
            for i, val in enumerate(galaxies):
                if val[1] > y:
                    galaxies[i] = (val[0], val[1] + expand_n)
            y += expand_n
        y += 1
    return galaxies


def duplicate_rows_cols(matrix, rows_to_duplicate, cols_to_duplicate):
    new_matrix = []
    for i, row in enumerate(matrix):
        new_row = []
        for j, val in enumerate(row):
            # Duplicate the column if necessary
            new_row.extend([val] * (cols_to_duplicate.count(j) + 1))
        # Duplicate the row if necessary
        new_matrix.extend([new_row] * (rows_to_duplicate.count(i) + 1))
    return new_matrix


def find_path_between_galaxies(galaxies):
    """find path between galaxies"""
    # find paths between each pair of galaxies
    paths = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            paths += find_manhattan_distance(galaxies[i], galaxies[j])
    return paths


def find_manhattan_distance(start, end):
    """find manhattan distance"""
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


# main
if __name__ == "__main__":
    # get input
    day = 11
    # data = get_input(day=day, test_data=True)
    data = get_input(day=day, test_data=False)

    # part a
    # new_universe = expand_universe(data)
    # galaxies = find_galaxies(new_universe)
    # paths = find_path_between_galaxies(galaxies)
    # print(f"sum of path lengths: {paths}")

    # part b
    old_universe, galaxies = read_universe(data)
    galaxies = expand_empty_rc(old_universe, galaxies, n=1e6)
    paths = find_path_between_galaxies(galaxies)
    print(f"sum of path lengths: {paths}")
