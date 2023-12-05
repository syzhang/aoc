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

def get_digit_word(data):
    """get first and last digit in word"""
    all_digits = []
    for line in data.split('\n'):
        if line:
            # parse digit words from line
            parsed_line = replace_spelled_numbers(line)
            print(parsed_line)
            # find digits
            digits = re.findall(r'\d+', parsed_line)
            digits_first, digits_last = parse_digits(digits)
            print(digits_first, digits_last)
            # convert to int
            combined_digits = int(str(digits_first) + str(digits_last))
            all_digits.append(combined_digits)
    print(all_digits)
    sum_digits = sum(all_digits)
    print(sum_digits)
    return sum_digits

def replace_spelled_numbers(line):
    """replace spelled numbers with digits"""
    digit_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
                    'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    # check if line contains spelled numbers from first letter
    print(line)
    if any(word in line for word in digit_dict.keys()):
        # print matched word
        word_list = []
        for word in digit_dict.keys():
            if word in line:
                word_list.append(word)
        # print(word_list)
        # reorder words according to position in line
        word_idx_dict = {}
        for word in word_list:
            word_idx = line.index(word)
            word_idx_dict[word] = word_idx
        reorder_word_list = sorted(word_idx_dict, key=word_idx_dict.get)
        print(reorder_word_list)
        
        # replace spelled numbers with digits
        for word in reorder_word_list:
            line = line.replace(word, str(digit_dict[word]))
    return line

# main
if __name__ == '__main__':
    # get input data
    # input_data = get_input(day=1, test_data=True, part='b')
    input_data = get_input(day=1, test_data=False)
    
    # solve
    # part a
    # get_digit(input_data)

    # part b
    get_digit_word(input_data)