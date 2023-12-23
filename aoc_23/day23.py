"""
day 23
"""

from collections import defaultdict
from utils import get_input
import sys

sys.setrecursionlimit(10000)  # Increase the recursion limit to 3000


def parse_grid(input):
    """parse grid"""
    grid = [x for x in input.split("\n") if x]
    return grid


def neighbours(grid, pos, is_slope):
    """neighbours"""
    cx, cy = pos
    match grid[cx][cy], is_slope:
        case ".", True:
            moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        case ">", True:
            moves = [(0, 1)]
        case "v", True:
            moves = [(1, 0)]
        case "<", True:
            moves = [(0, -1)]
        case "^", True:
            moves = [(-1, 0)]
        case _, False:
            moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # check if we are on the edge
    out = set()
    m = len(grid)
    n = len(grid[0])
    for dx, dy in moves:
        new_x = pos[0] + dx
        new_y = pos[1] + dy
        if new_x in range(m) and new_y in range(n) and grid[new_x][new_y] != "#":
            yield (new_x, new_y)


best = 0


def dfs(cur, path, pathset, grid, is_slope=True):
    """depth first search"""
    global best
    n = len(grid)
    m = len(grid[0])
    if cur == (n - 1, m - 2):
        best = max(best, len(path))
    for a in neighbours(grid, cur, is_slope):
        if a not in pathset:
            path.append(a)
            pathset.add(a)
            dfs(a, path, pathset, grid, is_slope)
            pathset.remove(a)
            path.pop(-1)

def get_graph(grid, is_slope=True):
    vertices = [(1, 0)]
    visited = set()
    graph = {}
    while vertices:
        vertex = vertices.pop()
        if vertex in visited:
            continue
        graph[vertex] = []
        for next_step in neighbours(grid, vertex, is_slope):
            length = 1
            prev = vertex
            position = next_step
            dead_end = False
            while True:
                neighbors = list(neighbours(grid, position, is_slope))
                if neighbors == [prev] and grid[position[1]][position[0]] in '<>^v':
                    dead_end = True
                    break
                if len(neighbors) != 2:
                    break
                for neighbor in neighbors:
                    if neighbor != prev:
                        length += 1
                        prev = position
                        position = neighbor
                        break
            if dead_end:
                continue
            graph[vertex].append((position, length))
            vertices.append(position)
        visited.add(vertex)
    return graph


def iter_hike_lengths(graph, goal):
    start = (0, 1)
    stack = [(start, 0, {start})]
    ls = []
    while stack:
        last, length, visited = stack.pop()
        if last == goal:
            ls.append(length)
            continue
        for new, edge_length in graph[last]:
            if new not in visited:
                stack.append((new, length + edge_length, visited | {new}))
    return ls

# main
if __name__ == "__main__":
    # input = get_input(day=23, test_data=True)
    input = get_input(day=23, test_data=False)
    # part a
    grid = parse_grid(input)
    # dfs((0, 1), [], set(), grid, is_slope=True)
    # print(best)
    # part b
    goal = len(grid) - 1, len(grid[0]) - 2
    graph = get_graph(grid, is_slope=False)
    print(max(iter_hike_lengths(graph, goal)))
