"""
day 9
"""
import math
from utils import get_input


def calc_extrapolation(line):
    """calculate extrapolation of line"""
    nums = list(map(int, line.split()))
    # diff until all zeros
    last_nums = []
    first_nums = []
    while True:
        last_nums.append(nums[-1])
        first_nums.append(nums[0])
        nums = diff_line(nums)
        if not any(nums):
            # print(nums)
            # print(last_nums)
            break
    return first_nums, last_nums


def extrapolate_a(last_nums):
    # extrapolate
    extrapolated = sum(last_nums)
    print(extrapolated)
    return extrapolated


def extrapolate_b(first_nums):
    # extrapolate
    for i, n in enumerate(first_nums[::-1]):
        if i == 0:
            tmp = n - 0
        else:
            tmp = n - tmp
    return tmp


def diff_line(nums):
    """calculate diff of line"""
    diff = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
    return diff


# main
if __name__ == "__main__":
    # get input
    day = 9
    # data = get_input(day=day, test_data=True)
    data = get_input(day=day, test_data=False)

    # part a
    all_first_nums = []
    all_last_nums = []
    for line in data.split("\n"):
        if line:
            first_nums, last_nums = calc_extrapolation(line)
            all_first_nums.append(first_nums)
            all_last_nums.append(last_nums)

    # extrapolate a
    # print(sum(extrapolate_a(l) for l in all_last_nums))

    # part b
    print(sum(extrapolate_b(f) for f in all_first_nums))
