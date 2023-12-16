"""
day 15
"""
import re
from utils import get_input


def get_string(data):
    """get string"""
    return data.split("\n")[0].split(",")


def hash_string(st):
    """hash string"""
    # find ascii value of each char
    ord_list = [ord(c) for c in st]
    # find current value
    current_value = 0
    for o in ord_list:
        current_value += o
        current_value = (current_value * 17) % 256
    return current_value


def move_boxes(stings):
    """moving boxes"""
    boxes = [{} for i in range(256)]
    # get label
    for x in stings:
        label = re.match(r"^[a-z]+", x).group(0)
        box = boxes[hash_string(label)]
        # = to insert, else to remove
        if "=" in x:
            box[label] = int(x.split("=")[1])
        else:
            box.pop(label, None)
    # calculate (1+box_number)*slot_number*focal_length
    sum_current = 0
    for box_num, box in enumerate(boxes):
        for slot_num, focal_length in enumerate(box.values()):
            tmp = (box_num + 1) * int(slot_num + 1) * focal_length
            sum_current += tmp
    print(sum_current)


# main
if __name__ == "__main__":
    # get input
    day = 15
    # data = get_input(day, test_data=True)
    data = get_input(day, test_data=False)

    # part a
    strings = get_string(data)
    # sum_current = sum(hash_string(st) for st in strings)
    # print(sum_current)

    # part b
    move_boxes(strings)
