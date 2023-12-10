"""
day 8
"""

import math
import re
from utils import get_input


def get_directions(data):
    """get directions from data"""
    directions, *mappings = data.split("\n\n")
    mappings = mappings[0].split("\n")
    # split mappings to current and next
    maps = {}
    locs = [m.split("=")[0].strip() for m in mappings]
    for i, l in enumerate(locs):
        if mappings[i]:
            tmp = mappings[i].split("=")[1].strip().split()
            # strip brackets and comma
            tmp = [x.strip("(),") for x in tmp]
            maps[l] = tmp
    return directions, maps


def follow_directions(start="AAA", end=None):
    """follow directions to get to ZZZ"""
    directions, maps = get_directions(data)
    steps = 0
    next = start
    while True:
        for d in directions:
            if end is not None and next == end:
                print(steps)
                return steps
            elif end is None and next[-1] == 'Z':
                print(steps)
                return steps
                
            if d == "L":
                next = maps[next][0]
            elif d == "R":
                next = maps[next][1]
            steps += 1

def find_starts_ends(maps):
    """find all start and end points"""
    starts = []
    ends = []
    for k, v in maps.items():
        if k.endswith('A'):
            starts.append(k)
        elif k.endswith('Z'):
            ends.append(k)
    return starts, ends

# main
if __name__ == "__main__":
    # get input
    day = 8
    # data = get_input(day=day, test_data=True)
    data = get_input(day=day, test_data=False)
    # get directions
    directions, mappings = get_directions(data)

    # part a
    # steps = follow_directions("AAA", "ZZZ")

    # part b
    starts, ends = find_starts_ends(mappings)
    counts = [follow_directions(s) for s in starts]
    # use least common multiple to find the number of steps, since we want to visit all ends from all starts
    print(math.lcm(*counts))


    
