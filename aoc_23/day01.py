"""
day 1
"""
import re
from utils import get_input

def get_digit(data):
    """get first and last digit of each line"""
    all_digits = []
    for line in data.split('\n'):
        if line:
            # extract digit from line
            digits = re.findall(r'\d+', line)
            # extract first and last digit
            digits_first, digits_last = parse_digits(digits)
            # convert to int
            combined_digits = int(str(digits_first) + str(digits_last))
            all_digits.append(combined_digits)
    print(all_digits)
    sum_digits = sum(all_digits)
    print(sum_digits)
    return sum_digits

def parse_digits(digits):
    """parse digits recursively"""
    # base case
    if len(digits) == 1:
        return digits[0][0], digits[0][-1]
    # recursive case
    else:
        return digits[0][0], parse_digits(digits[1:])[-1]

def replace_spelled_numbers(input_data):
    """replace spelled numbers with digits"""
    d = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
                    'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    input = [x for x in input_data.split('\n') if x]
    total = 0
    for line in input:
        first = find_digit(line, d)
        last = find_digit(line, d, True)
        total += int(str(first) + str(last or first))
        # print(line, first, last)
    print(total)

def find_digit(l, d, reverse=False):
    range_ = range(len(l), -1, -1) if reverse else range(len(l) + 1)

    # find first digit
    for i in range_:
        substr = l[i:] if reverse else l[:i]
        digit = next((int(ch) for ch in substr if ch.isdigit()), False)
        if not digit:
            digit = next((v for k, v in d.items() if k in substr), False)
        if digit:
            return digit
    return False

# main
if __name__ == '__main__':
    # get input data
    # input_data = get_input(day=1, test_data=True, part='b')
    input_data = get_input(day=1, test_data=False)
    
    # solve
    # part a
    # get_digit(input_data)

    # part b
    replace_spelled_numbers(input_data)