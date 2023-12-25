"""
day 25
"""

from utils import get_input
from math import prod
from igraph import Graph


def parse_connections(input):
    lines = [x for x in input.split("\n") if x]
    G = {v: e.split() for v, e in [l.split(":") for l in lines]}
    return G


def find_groups(G):
    ld = Graph.ListDict(G)
    mincut = ld.mincut()
    print(mincut)
    print(mincut.sizes())
    print(prod(mincut.sizes()))

# main
if __name__ == "__main__":
    # get input
    # input = get_input(day=25, test_data=True)
    input = get_input(day=25, test_data=False)
    # part a
    G = parse_connections(input)
    find_groups(G)
