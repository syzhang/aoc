"""
day 24
"""

import random
import statistics
from utils import get_input
from scipy.optimize import fsolve


def parse_input(input):
    """parse input"""
    lines = [x for x in input.split("\n") if x]
    pv = []
    for l in lines:
        p = tuple(map(int, l.split("@")[0].split(",")))
        v = tuple(map(int, l.split("@")[1].split(",")))
        pv.append((p, v))
    return pv

def line_intersection(P1, D1, P2, D2):
    # Calculate the determinant
    det = D1[0] * D2[1] - D1[1] * D2[0]
    if det == 0:
        return None, None, None  # Lines are parallel

    # Calculate the parameters t and u
    t = ((P2[0] - P1[0]) * D2[1] - (P2[1] - P1[1]) * D2[0]) / det
    u = ((P2[0] - P1[0]) * D1[1] - (P2[1] - P1[1]) * D1[0]) / det

    # Calculate the intersection point
    intersection = [P1[0] + t * D1[0], P1[1] + t * D1[1]]

    return intersection, t, u

def find_intersect(pv, test_x_range, test_y_range, xy_only=True):
    """part a"""
    total = 0
    for i in range(len(pv)):
        for j in range(i + 1, len(pv)):
            p1, v1 = pv[i]
            p2, v2 = pv[j]
            if xy_only:
                p1 = (p1[0], p1[1])
                p2 = (p2[0], p2[1])
                v1 = (v1[0], v1[1])
                v2 = (v2[0], v2[1])
            intersection, t, u = line_intersection(p1, v1, p2, v2)
            if intersection:
                # within range and forward in time intersect
                if intersection[0] > test_x_range[0] and intersection[0] < test_x_range[1] and intersection[1] > test_y_range[0] and intersection[1] < test_y_range[1] and t > 0 and u > 0:
                    # print("intersect")
                    total += 1
    return total

def equations(vars, object_positions, object_velocities):
    # https://github.com/guiambros/aoc-2023/blob/main/day24/day24.py#L9
    P0x, P0y, P0z, V0x, V0y, V0z, t1, t2, t3 = vars
    # Equations for each object at interception time
    eqs = []
    for i in range(3):
        posx, posy, posz = object_positions[i]
        velx, vely, velz = object_velocities[i]
        t = [t1, t2, t3][i]
        eqs.append(P0x + V0x * t - (posx + velx * t))
        eqs.append(P0y + V0y * t - (posy + vely * t))
        eqs.append(P0z + V0z * t - (posz + velz * t))

    return eqs

def solve_numerically(pv):
    # random sample of 3 objects
    R = random.sample(pv, 3)
    pos_x1, pos_y1, pos_z1 = R[0][0]
    vel_x1, vel_y1, vel_z1 = R[0][1]

    pos_x2, pos_y2, pos_z2 = R[1][0]
    vel_x2, vel_y2, vel_z2 = R[1][1]

    pos_x3, pos_y3, pos_z3 = R[2][0]
    vel_x3, vel_y3, vel_z3 = R[2][1]

    # Initial positions and velocities of the objects
    object_positions = [
        [pos_x1, pos_y1, pos_z1],
        [pos_x2, pos_y2, pos_z2],
        [pos_x3, pos_y3, pos_z3],
    ]
    object_velocities = [
        [vel_x1, vel_y1, vel_z1],
        [vel_x2, vel_y2, vel_z2],
        [vel_x3, vel_y3, vel_z3],
    ]

    # Initial guesses for P0x, P0y, P0z, V0x, V0y, V0z, t1, t2, t3
    initial_guesses = [
        pos_x1 / 2,
        pos_y1 / 2,
        pos_z1 / 2,
        vel_x1 / 2,
        vel_y1 / 2,
        vel_z1 / 2,
        500000000000,
        500000000000,
        500000000000,
    ]

    # Solve the system of equations
    solution = fsolve(
        equations, initial_guesses, args=(object_positions, object_velocities), xtol=1e-12
    )
    return solution

def partb_numerically():
    all_res = []
    for i in range(1000):
        res = sum(solve_numerically(pv)[:3])
        print(f"Solving pt2 numerically -- #{i} -- {res}")
        all_res.append(res)
    mode = statistics.mode(all_res)
    return int(mode)

# main
if __name__ == "__main__":
    # input = get_input(day=24, test_data=True)
    input = get_input(day=24, test_data=False)
    # part a
    pv = parse_input(input)
    # test_x_range = [7, 27]
    # test_x_range = [200000000000000, 400000000000000]
    # test_y_range = test_x_range
    # print(find_intersect(pv, test_x_range, test_y_range, xy_only=True))
    # part b
    mode_inits = partb_numerically()
    print(mode_inits)