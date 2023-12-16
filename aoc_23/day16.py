"""
day 16
"""

from collections import deque
from utils import get_input

def get_grid(data):
    """get grid from data"""
    grid = data.split("\n")
    # get rid of empty lines
    grid = [x for x in grid if x]
    return grid

def pass_light(grid, i, j, di, dj):
    """pass light through grid"""
    # encounters
    m, n = len(grid), len(grid[0])
    # double ended queue
    q = deque([(i, j, di, dj)])
    visited = set()
    while q:
        i, j, di, dj = q.popleft()
        if (i, j, di, dj) in visited or i < 0 or i >= m or j < 0 or j >= n:
            continue
        visited.add((i, j, di, dj))
        if grid[i][j] == "-" and di != 0:
            q.append((i, j+1, 0, 1))
            q.append((i, j-1, 0, -1))
        elif grid[i][j] == "|" and dj != 0:
            q.append((i+1, j, 1, 0))
            q.append((i-1, j, -1, 0))
        elif grid[i][j] == "/":
            q.append((i-dj, j-di, -dj, -di))
        elif grid[i][j] == "\\":
            q.append((i+dj, j+di, dj, di))
        else:
            q.append((i+di, j+dj, di, dj))
    return len(set((i, j) for i, j, _, _ in visited))


def pass_light_from_all_edges(grid):
    """pass light from all edges"""
    m, n = len(grid), len(grid[0])
    left_edge = [(i, 0, 0, 1) for i in range(m)]
    right_edge = [(i, n-1, 0, -1) for i in range(m)]
    top_edge = [(0, j, 1, 0) for j in range(n)]
    bottom_edge = [(m-1, j, -1, 0) for j in range(n)]
    all_edges = left_edge + right_edge + top_edge + bottom_edge
    max_energised = 0
    for i, j, di, dj in all_edges:
        # print(i, j, di, dj)
        tmp = pass_light(grid, i, j, di, dj)
        max_energised = max(max_energised, tmp)
    return max_energised

# main
if __name__ == "__main__":
    # get input
    day = 16
    # data = get_input(day, test_data=True)
    data = get_input(day, test_data=False)

    # part a
    grid = get_grid(data)
    # energised = pass_light(grid, 0, 0, 0, 1)
    # print(energised)
    
    # part b
    energised = pass_light_from_all_edges(grid)
    print(energised)
