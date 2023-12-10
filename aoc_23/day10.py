"""
day 10
"""

from queue import Queue
from utils import get_input


def map_board(data):
    """map board with relevant rules"""
    board = data.strip().split()
    # possible moves
    n = {
        "|": [(0, -1), (0, 1)],
        "-": [(-1, 0), (1, 0)],
        "L": [(0, -1), (1, 0)],
        "J": [(0, -1), (-1, 0)],
        "7": [(-1, 0), (0, 1)],
        "F": [(1, 0), (0, 1)],
    }
    return board, n


def part_a(board, n):
    """find max distance from start"""
    # find start
    x, y = None, None
    for yi, line in enumerate(board):
        for xi, c in enumerate(line):
            if c == "S":
                x, y = xi, yi
                break
    print(f"Start loc {x,y}")

    # explore moves
    # using a queue follows first in first out
    possible_moves = Queue()
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        c = board[y + dy][x + dx]
        if c in n:
            for dx2, dy2 in n[c]:
                # check if the move is valid
                if x == x + dx + dx2 and y == y + dy + dy2:
                    possible_moves.put((1, (x + dx, y + dy)))

    dists = {(x, y): 0}

    # get valid positions and distance
    while not possible_moves.empty():
        d, (x, y) = possible_moves.get()
        if (x, y) in dists:
            continue
        # append distance
        dists[(x, y)] = d
        # add to total distance
        if board[y][x] in n.keys():
            for dx, dy in n[board[y][x]]:
                possible_moves.put((d + 1, (x + dx, y + dy)))

    print(f"Max distance: {max(dists.values())}")
    return dists


def part_b(board, dists):
    """find number of enclosed areas"""
    # board size
    w = len(board[0])
    h = len(board)

    inside_count = 0
    # make a copy of board with all .
    board_copy = "." * w
    board_copy = [board_copy] * h
    for y, line in enumerate(board):
        for x, c in enumerate(line):
            if (x, y) in dists:
                continue

            crosses = 0
            x2, y2 = x, y

            while x2 < w and y2 < h:
                c2 = board[y2][x2]
                if (x2, y2) in dists and c2 != "L" and c2 != "7":
                    board_copy[y2] = (
                        board_copy[y2][:x2] + "X" + board_copy[y2][x2 + 1 :]
                    )
                    crosses += 1
                x2 += 1
                y2 += 1

            if crosses % 2 == 1:
                inside_count += 1

    print(f"Inside count: {inside_count}")


# main
if __name__ == "__main__":
    # get input
    day = 10
    # data = get_input(day=day, test_data=True)
    data = get_input(day=day, test_data=False)

    # part a
    board, n = map_board(data)
    dists = part_a(board, n)

    # part b
    part_b(board, dists)
