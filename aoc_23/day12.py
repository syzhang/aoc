"""
day 12
"""
from utils import get_input
from functools import cache

def get_info(data):
    """get info"""
    info = [x.split() for x in data.splitlines()]
    return info

def find_combinations(info):
    """find combinations"""
    counts = 0
    for i, (lava, springs) in enumerate(info):
        counts += recurse(lava, tuple(map(int, springs.split(','))))
    print(f"part a: {counts}")

def find_combinations_b(info):
    """find combinations"""
    counts = 0
    for i, (lava, springs) in enumerate(info):
        lava5 = '?'.join([lava] * 5)
        springs5 = tuple(map(int, springs.split(','))) * 5
        counts += recurse(lava5, springs5)
    print(f"part b: {counts}")

@cache
def recurse(lava, springs, result=0):
    """recurse lava and springs to find combinations"""
    if not springs:
        return '#' not in lava
    # find next spring
    current, springs = springs[0], springs[1:]
    for i in range(len(lava) - sum(springs) - len(springs) - current + 1):
        if "#" in lava[:i]:
            break
        nxt = i + current
        if nxt <= len(lava):
            if '.' not in lava[i : nxt]:
                if lava[nxt : nxt + 1] != "#":
                    result += recurse(lava[nxt + 1:], springs)
    return result

# main
if __name__ == "__main__":
    # get input
    day = 12
    # data = get_input(day, test_data=True)
    data = get_input(day, test_data=False)

    # part a
    # find_combinations(get_info(data))

    # part b
    find_combinations_b(get_info(data))
