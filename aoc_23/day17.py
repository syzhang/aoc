"""
day 17
"""
import heapq
from utils import get_input


def get_grid(data):
    """get grid from data"""
    grid = data.split("\n")
    # get rid of empty lines
    grid = [x for x in grid if x]
    return grid


def dijkstra(grid, min_dist, max_dist):
    """dijkstra, heappop removes and returns the smallest element from the heap, ensuring that the heap property is maintained"""
    # cost, x, y, disallowedDirection
    q = [(0, 0, 0, -1)]
    seen = set()
    costs = {}
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while q:
        cost, x, y, dd = heapq.heappop(q)
        if x == len(grid) - 1 and y == len(grid[0]) - 1:  # goal x, goal y
            return cost
        if (x, y, dd) in seen:
            continue
        seen.add((x, y, dd))
        for direction in range(4):
            costincrease = 0
            if direction == dd or (direction + 2) % 4 == dd:
                # can't repeat the same direction or go back
                continue
            for distance in range(1, max_dist + 1):
                next_x = x + directions[direction][0] * distance
                next_y = y + directions[direction][1] * distance
                if inrange((next_x, next_y), grid):
                    costincrease += int(grid[next_x][next_y])
                    if distance < min_dist:
                        continue
                    new_cost = cost + costincrease
                    if costs.get((next_x, next_y, direction), 1e100) <= new_cost:
                        continue
                    costs[(next_x, next_y, direction)] = new_cost
                    heapq.heappush(q, (new_cost, next_x, next_y, direction))
    return -1


def inrange(pos, grid):
    """in range"""
    return pos[0] in range(len(grid)) and pos[1] in range(len(grid[0]))


# main
if __name__ == "__main__":
    # get input
    # input = get_input(day=17, test_data=True)
    input = get_input(day=17, test_data=False)

    # part a
    grid = get_grid(input)
    # cost = dijkstra(grid, min_dist=1, max_dist=3)
    # print(cost)

    # part b
    cost = dijkstra(grid, min_dist=4, max_dist=10)
    print(cost)
