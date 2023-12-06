"""
day 3
"""
import math as m
import re
from utils import get_input

def find_chars(input_data):
    """find the index of the number"""
    # split data into lines
    board = list(input_data.splitlines())
    # find the index of numbers in 2d list
    chars = {(r, c): [] for r in range(140) for c in range(140)
                        if board[r][c] not in '01234566789.'}

    # find the edge of each number
    for r, row in enumerate(board):
        for n in re.finditer(r'\d+', row):
            print(n)
            # find the edge of each number
            edge = {(r, c) for r in (r-1, r, r+1)
                        for c in range(n.start()-1, n.end()+1)}
            # set of edge and chars
            for o in edge & chars.keys():
                chars[o].append(int(n.group()))
    return chars

# main
if __name__ == "__main__":
    # get input data
    # input_data = get_input(day=3, test_data=True)
    input_data = get_input(day=3, test_data=False)

    # solve
    # part a
    chars = find_chars(input_data)
    print(sum(sum(p)    for p in chars.values()))

    # part b
    print(sum(m.prod(p) for p in chars.values() if len(p)==2))

