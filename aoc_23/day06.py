"""
day 6
"""
import re
from utils import get_input
from functools import reduce


def get_race_info(data):
    """get race distance and time"""
    lines = data.splitlines()
    # time
    time = re.findall(r"\d+", lines[0])
    # distance
    distance = re.findall(r"\d+", lines[1])
    return list(map(int, time)), list(map(int, distance))


def count_possible_wins(time, distance):
    """count the number of possible wins"""
    race_counts = []
    for i, t in enumerate(time):
        dist = distance[i]
        count = 0
        for speed in range(t):
            remain_time = t - speed
            possible_dist = speed * remain_time
            if possible_dist > dist:
                count += 1
        race_counts.append(count)
    return race_counts


def get_new_race_info(data):
    """get new race distance and time"""
    lines = data.splitlines()
    # time
    time = re.findall(r"\d+", lines[0])
    # distance
    distance = re.findall(r"\d+", lines[1])
    return [int("".join(time))], [int("".join(distance))]


# main
if __name__ == "__main__":
    # get input data
    day = 6
    # input_data = get_input(day=day, test_data=True)
    input_data = get_input(day=day, test_data=False)

    # part a
    # time, dist = get_race_info(input_data)

    # part b
    time, dist = get_new_race_info(input_data)

    wins = count_possible_wins(time, dist)
    # multiply numbers in wins
    print(reduce(lambda x, y: x * y, wins))
