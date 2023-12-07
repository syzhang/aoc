"""
day 4
"""
import re
from utils import get_input


def find_winning_numbers(data):
    """find the winning numbers"""
    # split data into lines
    lines = list(data.splitlines())
    # find the index of numbers in 2d list
    winning_nums, candidate_nums = split_win_candidate(lines)
    # check how many of the numbers are winning
    points = 0
    for i, c in enumerate(candidate_nums):
        winning_candidates = [n for n in c if n in winning_nums[i]]
        if len(winning_candidates) == 0:
            continue
        points += 2 ** (len(winning_candidates) - 1)
        # print(winning_candidates, points)
    print(points)
    return points


def find_scratchcards(data):
    """find the scratchcards"""
    # split data into lines
    lines = list(data.splitlines())
    # find the index of numbers in 2d list
    winning_nums, candidate_nums = split_win_candidate(lines)
    # check how many of the numbers are winning, at least one card
    win_counts = {n: 1 for n in range(1, len(lines) + 1)}
    for i, c in enumerate(candidate_nums):
        current_card = i + 1
        winning_candidates = [n for n in c if n in winning_nums[i]]
        # iterate through next cards
        for next_card in range(
            current_card + 1, current_card + len(winning_candidates) + 1
        ):
            if next_card not in win_counts:
                win_counts[next_card] = 0
            win_counts[next_card] += 1 * win_counts[current_card]
    print(sum(win_counts.values()))
    return win_counts


def split_win_candidate(lines):
    """split the input data into winning numbers and candidate numbers"""
    winning_nums = [l.split(":")[1].split("|")[0] for l in lines]
    candidate_nums = [l.split(":")[1].split("|")[1] for l in lines]
    winning_nums = [list(map(int, re.findall(r"\d+", n))) for n in winning_nums]
    candidate_nums = [list(map(int, re.findall(r"\d+", n))) for n in candidate_nums]
    return winning_nums, candidate_nums


# main
if __name__ == "__main__":
    # get input data
    # input_data = get_input(day=4, test_data=True)
    input_data = get_input(day=4, test_data=False)

    # solve
    # part a
    points = find_winning_numbers(input_data)

    # part b
    win_counts = find_scratchcards(input_data)
