"""
day 20
"""
from collections import defaultdict
import math
from utils import get_input


def parse(input):
    """parse input"""
    flips = defaultdict(list)
    conjs = defaultdict(list)
    broadcasts = []
    for line in input.split("\n"):
        if not line:
            continue
        tmp = line.strip().split()
        if tmp[0].startswith("%"):
            current = tmp[0][1:]
            for t in tmp[2:]:
                flips[current].append(t.strip(","))
        elif tmp[0].startswith("&"):
            current = tmp[0][1:]
            for t in tmp[2:]:
                conjs[current].append(t.strip(","))
        elif tmp[0] == "broadcaster":
            for t in tmp[2:]:
                broadcasts.append(t.strip(","))

    return flips, conjs, broadcasts


def part_a(flips, conjs, broadcasts):
    """part a"""
    flip_states = {}
    conj_states = defaultdict(dict)
    # flip states
    for f in flips.keys():
        flip_states[f] = False
        for t in flips[f]:
            if t in conjs.keys():
                conj_states[t][f] = False
    # conj states
    for k, v in conjs.items():
        for c in v:
            if c in conjs.keys():
                conj_states[c][k] = False

    # run
    lows = 0
    highs = 0
    for _ in range(1000):
        pulse_queue = [("broadcaster", False, "button")]
        while len(pulse_queue) > 0:
            nxt = pulse_queue.pop(0)
            dst, pulse, src = nxt
            if pulse == True:
                highs += 1
            else:
                lows += 1
            if dst == "broadcaster":
                for b in broadcasts:
                    pulse_queue.append((b, pulse, dst))
            elif dst in flip_states.keys():
                if pulse == False:
                    flip_states[dst] = not flip_states[dst]
                    for f in flips[dst]:
                        pulse_queue.append((f, flip_states[dst], dst))
            elif dst in conj_states.keys():
                conj_states[dst][src] = pulse
                rest = not all([v for v in conj_states[dst].values()])
                for f in conjs[dst]:
                    pulse_queue.append((f, rest, dst))
    return lows, highs


def part_b(flips, conjs, broadcasts):
    """part b"""
    # rx to get low pulse, all inputs needs high pulse because it's conj
    flip_states = {}
    conj_states = defaultdict(dict)
    # flip states
    for f in flips.keys():
        flip_states[f] = False
        for t in flips[f]:
            if t in conjs.keys():
                conj_states[t][f] = False
    # conj states
    for k, v in conjs.items():
        for c in v:
            if c in conjs.keys():
                conj_states[c][k] = False

    # run
    lows = 0
    highs = 0
    seens = defaultdict(list)
    counts = 0
    for i in range(int(100000000000000000)):
        if i % 10000 == 0 and i > 0:
            cycles = []
            for k, v in seens.items():
                v2 = []
                for i in range(len(v)-1):
                    v2.append(v[i + 1] - v[i])
                cycles.append(v2[0])
            return math.lcm(*cycles) # find all cycles then calculate least common multiple of all cycles, min number of pulses to get to final state
        pulse_queue = [("broadcaster", False, "button")]
        while len(pulse_queue) > 0:
            nxt = pulse_queue.pop(0)
            dst, pulse, src = nxt
            if src in ["nb", "vc", "vg", "ls"] and pulse == True:
                seens[src].append(i + 1)
            if pulse == True:
                highs += 1
            else:
                lows += 1
            if dst == "rx" and pulse == False:
                return i + 1
            if dst == "broadcaster":
                for b in broadcasts:
                    pulse_queue.append((b, pulse, dst))
                continue
            elif dst in flip_states.keys():
                if pulse == False:
                    flip_states[dst] = not flip_states[dst]
                    for f in flips[dst]:
                        pulse_queue.append((f, flip_states[dst], dst))
            elif dst in conj_states.keys():
                conj_states[dst][src] = pulse
                rest = not all([v for v in conj_states[dst].values()])
                for f in conjs[dst]:
                    pulse_queue.append((f, rest, dst))
    return 0

# main
if __name__ == "__main__":
    # get input
    # input = get_input(day=20, test_data=True)
    input = get_input(day=20, test_data=False)

    # part a
    flips, conjs, broadcasts = parse(input)
    # lows, highs = part_a(flips, conjs, broadcasts)
    # print(lows * highs)

    # part b
    print(part_b(flips, conjs, broadcasts))