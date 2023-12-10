"""
day 7
"""

from enum import Enum
import math
import re
from utils import get_input


def get_hands(data):
    """get suit and bid"""
    lines = data.splitlines()
    # suit and bid
    hands = []
    for l in lines:
        if l:
            suit, bid = l.split(" ")
            hands.append((suit, int(bid)))
    return hands


class ordering(Enum):
    normal = "AKQJT98765432"[::-1]
    jokers = "AKQT98765432J"[::-1]


def get_ordering(hands, order_by="normal"):
    """order hands by ordering"""
    if order_by == "normal":
        return [list(map(ordering.normal.value.index, x[0])) for x in hands]
    elif order_by == "jokers":
        return [list(map(ordering.jokers.value.index, x[0])) for x in hands]


def entropy(hands):
    """calculate entropy of hand, less different/higher scored hands have lower entropy"""
    ents = []
    for h in hands:
        ent = 0
        for c in set(h):
            p = h.count(c) / len(h)
            ent -= -p * math.log(p)
        ents.append(ent)
    return ents


def entropy_with_joker(hands):
    """calculate entropy of hand, less different/higher scored hands have lower entropy"""
    ents = []
    for h in hands:
        try:
            top = sorted(
                h[0].replace("J", ""),
                key=lambda c: h[0].count(c),
            )[-1]
            tmp = h[0].replace("J", top)
        except:  # JJJJJ
            tmp = h[0]
        ents.append(entropy([tmp])[0])
    return ents


def sort_hands(hands, hands_ordered, entropies):
    """sort hands by entropy and ordering"""
    return sorted(zip(hands, hands_ordered, entropies), key=lambda x: (x[2], x[1]))


def get_winnings(hands_sorted):
    """get winnings"""
    winnings = 0
    for i, h in enumerate(hands_sorted):
        winnings += h[0][1] * (i + 1)
    return winnings


# main
if __name__ == "__main__":
    # get input data
    day = 7
    # input_data = get_input(day=day, test_data=True)
    input_data = get_input(day=day, test_data=False)

    # part a
    hands = get_hands(input_data)
    # hands_ordered = get_ordering(hands)
    # ent = entropy(hands_ordered)
    # hands_sorted = sort_hands(hands, hands_ordered, ent)
    # winnings = get_winnings(hands_sorted)
    # print(winnings)

    # part 2
    ent = entropy_with_joker(hands)
    hands_ordered = get_ordering(hands, order_by="jokers")
    hands_sorted = sort_hands(hands, hands_ordered, ent)
    winnings = get_winnings(hands_sorted)
    print(winnings)
