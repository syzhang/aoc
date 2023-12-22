"""
day 22
"""

from utils import get_input


def parse_input(input):
    """parse input"""
    blocks = []
    for line in input.split("\n"):
        if not line:
            continue
        block = parse_block(line)
        blocks.append(block)
    return blocks


def parse_block(line):
    """parse block"""
    return [(int(n) for n in xyz.split(",")) for xyz in line.split("~")]


def map_bricks(blocks):
    """map bricks"""
    bricks = []
    for block in blocks:
        (x1, y1, z1), (x2, y2, z2) = block
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        z1, z2 = sorted([z1, z2])
        bricks.append((x1, y1, z1, x2, y2, z2))

    # sort z order, how far away from ground
    bricks.sort(key=lambda x: x[2])
    # max range in each dimension
    max_x = max([b[3] for b in bricks]) + 1
    max_y = max([b[4] for b in bricks]) + 1
    max_z = max([b[5] for b in bricks]) + 1

    # simulate stack
    stack = [[[None for _ in range(max_z)] for _ in range(max_y)] for _ in range(max_x)]
    # simulate fall
    supported_by = {}
    for brick_id, (x1, y1, z1, x2, y2, z2) in enumerate(bricks):
        # for each brick, check if it can fall
        for z in range(max_z):
            tmp = set(
                stack[x][y][z] for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)
            )
            support = tmp - {None}
            if support:
                supported_by[brick_id] = support
                break
        # add block above
        new_z = z2 - z1 + 1
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                for z_ in range(z - new_z, z):
                    stack[x][y][z_] = brick_id

    return bricks, supported_by


def part_a(bricks, supported_by):
    # count bricks that are supported by one other brick, they cannot be removed
    indispensible = set.union(*[x for x in supported_by.values() if len(x) == 1])
    return len(bricks) - len(indispensible)


def part_b(bricks, supported_by):
    # find number of bricks will fall by removing each brick
    n_bricks = len(bricks)
    indispensible = set.union(*[x for x in supported_by.values() if len(x) == 1])
    n_falls = 0
    for brick_id in indispensible:
        # remove brick
        disintegrates = set([brick_id])
        # check how mnay bricks will fall
        for j in range(brick_id + 1, n_bricks):
            if j in supported_by and supported_by[j].issubset(disintegrates):
                disintegrates.add(j)
        n_falls += len(disintegrates) - 1
    return n_falls


# main
if __name__ == "__main__":
    # get input
    # input = get_input(day=22, test_data=True)
    input = get_input(day=22, test_data=False)
    # part a
    blocks = parse_input(input)
    bricks, supported_by = map_bricks(blocks)
    # can_remove = part_a(bricks, supported_by)
    # print(can_remove)
    # part b
    n_falls = part_b(bricks, supported_by)
    print(n_falls)
