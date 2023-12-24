"""
day 10
"""

import operator
from queue import Queue
from utils import get_input


def map_board(data):
    """map board with relevant rules"""
    board = data.strip().split()
    # possible moves
    pipe_dir = {
        "|": ["N", "S"],
        "-": ["E", "W"],
        "L": ["N", "E"],
        "J": ["N", "W"],
        "7": ["S", "W"],
        "F": ["S", "E"],
    }
    delta_d = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}
    # n = {k: [delta_d[x] for x in v] for k, v in pipe_dir.items()}
    return board, pipe_dir, delta_d


def part_a(board, pipe_dir, delta_d):
    """find max distance from start"""
    # find start
    start_pos = [(r, c) for r, row in enumerate(board) for c, x in enumerate(row) if x == "S"][0]
    print(f"Start loc {start_pos}")

    # explore moves
    prev_pos = start_pos
    path = []
    path.append(start_pos)
    pos = tuple(map(operator.add, prev_pos, delta_d["E"]))
    cnt = 1
    while pos != start_pos:
        path.append(pos)
        pipe = board[pos[0]][pos[1]]
        if pipe == "S":
            print(f"Back to start {pos}")
            break
        pos, prev_pos = move(pos, pipe, prev_pos, pipe_dir, delta_d)
        cnt += 1
    print(f"Max distance: {cnt // 2}")
    return cnt//2, path


def move(pos, dirs, prev_pos, pipe_dir, delta_d):
    orig_pos = pos
    potential = []
    for d in pipe_dir[dirs]:
        potential.append(tuple(map(operator.add, pos, delta_d[d])))
    pos = [p for p in potential if p != prev_pos][0]
    return pos, orig_pos

def part_b(board, pipe_dir, delta_d, path):
    # Shoelace formula
    # https://en.wikipedia.org/wiki/Shoelace_formula
    def shoelace_area(points):
        n = len(points)
        res = 0
        for i in range(n):
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % n]
            res += x1 * y2 - x2 * y1
        return abs(res // 2)

    # Pick's theorem
    # https://en.wikipedia.org/wiki/Pick%27s_theorem
    b, path = part_a(board, pipe_dir, delta_d)
    i = shoelace_area(path) - b + 1
    return i


# main
if __name__ == "__main__":
    # get input
    day = 10
    # data = get_input(day=day, test_data=True)
    data = get_input(day=day, test_data=False)

    # part a
    board, pipe_dir, delta_d = map_board(data)
    path = part_a(board, pipe_dir, delta_d)

    # part b
    enclosed_points = part_b(board, pipe_dir, delta_d, path)
    print(f"Enclosed points: {enclosed_points}")