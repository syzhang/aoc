"""
day 18
"""

from utils import get_input


def get_info(data):
    """get edge"""
    edge = data.split("\n")
    # get rid of empty lines
    edge = [x for x in edge if x]
    # get direction, step, colour
    info = []
    for e in edge:
        direction, steps, colour = e.split(" ")
        info.append((direction, int(steps), colour))
    return info


def dig_edges(info, directions):
    """dig edges"""
    edges = set()
    location = (0, 0)  # start at (0, 0)
    edges.add(location)
    xs = []
    ys = []
    for d, s, _ in info:
        x, y = directions[d]
        for i in range(s + 1):
            edges.add((location[0] + i * x, location[1] + i * y))
        location = (location[0] + s * x, location[1] + s * y)
        xs.append(location[0])
        ys.append(location[1])
    return edges, xs, ys


def polygon_area(xs, ys):
    # https://en.wikipedia.org/wiki/Shoelace_formula
    return 0.5 * abs(
        sum(xs[i] * ys[i + 1] - xs[i + 1] * ys[i] for i in range(-1, len(xs) - 1))
    )


def get_area(edges, xs, ys):
    """get area"""
    # https://en.wikipedia.org/wiki/Pick's_theorem
    # i be the number of integer points interior to the polygon,
    # b be the number of integer points on its boundary (including both vertices and points along the sides). Then the area A of this polygon
    A = polygon_area(xs, ys)
    b = len(edges)
    # A = i + b/2 - 1 -> i = A + 1 - b/2
    assert b % 2 == 0
    I = A + 1 - b // 2
    print(I + b)  # add the number of edges


def convert_hex(data):
    """convert hex info"""
    edge = data.split("\n")
    # get rid of empty lines
    edge = [x for x in edge if x]
    # get direction, step, colour
    info = []
    colour = 0
    for e in edge:
        hx = e.split(" ")[-1].strip("()#")
        direction = int(hx[-1])
        steps = int(hx[:-1], 16)
        info.append((direction, int(steps), colour))
    return info


# main
if __name__ == "__main__":
    # get input
    # input = get_input(day=18, test_data=True)
    input = get_input(day=18, test_data=False)

    # part a
    # info = get_info(input)
    # directions = {"U": (0, -1), "R": (1, 0), "D": (0, 1), "L": (-1, 0)}
    # edges, xs, ys = dig_edges(info, directions=directions)
    # get_area(edges, xs, ys)

    # part b
    info = convert_hex(input)
    directions = {3: (0, -1), 0: (1, 0), 1: (0, 1), 2: (-1, 0)}
    edges, xs, ys = dig_edges(info, directions=directions)
    get_area(edges, xs, ys)
