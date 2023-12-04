"""
utils
"""
import os

def get_input(day, test_data=False, part=None):
    """read input file"""
    # parent folder
    parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # input file
    if test_data:
        if part is not None:
            input_file = os.path.join(parent, 'test_data', f'day{day:02}{part}.txt')
        else:
            input_file = os.path.join(parent, 'test_data', f'day{day:02}.txt')
    else:
        input_file = os.path.join(parent, 'data', f'day{day:02}.txt')
    # read input file
    with open(input_file) as input_file:
        input_data = input_file.read()
    return input_data