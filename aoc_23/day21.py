"""
day 21
"""
from collections import defaultdict
import re
from utils import get_input
from collections import deque


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
    print(len(visited))
    return visited


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

def parse_input(data):
    # Find the start point, and then split the input into a nested list and return the start point and the garden map
    data_list = data.splitlines()
    for idx, line in enumerate(data_list):
        start = re.search(r'S', line)
        if start is not None:
            start = (start.start(), idx)
            break
    data_list = [list(line) for line in data_list]
    return (start, data_list)

def possible_points(point, garden_map):
    # Loop over all possible directions, and yield each possible new point
    # Check the remainder of the point axis' divided by 131 to continue moving outward infinitely for part 2
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    for d in directions:
        new_point = (point[0] + d[0], point[1] + d[1])
        if garden_map[new_point[1] % 131][new_point[0] % 131] != '#':  # Make sure it wasn't a rock
            yield new_point
                
def bfs(point, garden_map, max_dist):
    # Use the Breadth first search to find the number of points hit each step, and return the dictionary with key of number of steps taken, 
    # and value of number of points hit
    tiles = defaultdict(int)
    visited = set()
    queue = [(point, 0)]
    while queue:  # End when the queue is empty
        curr_point, dist = queue.pop(0)
        if dist == (max_dist + 1) or curr_point in visited:  # Don't include points that have already been visited
            continue

        tiles[dist] += 1
        visited.add(curr_point)

        for next_point in possible_points(curr_point, garden_map):  # Loop over possible points and add to queue
            queue.append((next_point, (dist + 1)))
    return tiles

def calculate_possible_spots(start, garden_map, max_steps):
    # Get the output from bfs, and then return the sum of all potential stopping points in the tiles output based on even numbers
    tiles = bfs(start, garden_map, max_steps)
    return sum(amount for distance, amount in tiles.items() if distance % 2 == max_steps % 2)

def quad(y, n):
    # Use the quadratic formula to find the output at the large steps based on the first three data points
    a = (y[2] - (2 * y[1]) + y[0]) // 2
    b = y[1] - y[0] - a
    c = y[0]
    return (a * n**2) + (b * n) + c

def part2(parsed_data):
    # https://github.com/CalSimmon/advent-of-code/blob/main/2023/day_21/solution.py
    # Calculate the first three data points for use in the quadratic formula, and then return the output of quad
    goal = 26501365
    size = len(parsed_data[1])
    edge = size // 2

    y = [calculate_possible_spots(*parsed_data, (edge + i * size)) for i in range(3)]
    
    return quad(y, ((goal - edge) // size))

# main
if __name__ == "__main__":
    # get input
    # input = get_input(day=21, test_data=True)
    input = get_input(day=21, test_data=False)

    # part a
    # grid, start = parse_grid(input)
    # visited = part_a(grid, [start], steps=64)
    # print(visited)

    # part b
    parsed_data = parse_input(input)
    print(part2(parsed_data))
