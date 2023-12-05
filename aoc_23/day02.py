"""
day 2
"""
import re
from utils import get_input

def parse_game_data(data):
    """parse game data"""
    # split data into lines
    lines = data.split('\n')
    # remove game id from line
    parsed_lines = []
    for l in lines:
        if l:
            tmp = l.split(':')[1:][0]
            parsed_lines.append(tmp)
    # parse each observation with ; as delimiter
    parsed_data = []
    for line in parsed_lines:
        if line:
            obs = line.split(';')
            parsed_data.append(obs)
    # put parsed data into dict
    colours = ['red', 'green', 'blue']
    all_data = []
    for obs in parsed_data:
        game_data = []
        # parse colour with , as delimiter
        for ob in obs:
            parsed_colour = ob.split(',')
            # put parsed colour into dict and number of balls as value
            colour_dict = {}
            for i, c in enumerate(parsed_colour):
                if any(colour in c for colour in colours):
                    colour = re.findall(r'[a-z]+', c)[0]
                    balls = re.findall(r'\d+', c)[0]
                    colour_dict[colour] = int(balls)
            # put parsed colour dict into game data
            game_data.append(colour_dict)
        # find max balls for each colour
        max_balls = count_max_balls(game_data)
        all_data.append(max_balls)
    return all_data

def count_max_balls(game_data):
    """get max balls"""
    # get max balls for each colour
    max_balls = {}
    for obs in game_data:
        for colour, balls in obs.items():
            if colour in max_balls:
                if balls > max_balls[colour]:
                    max_balls[colour] = balls
            else:
                max_balls[colour] = balls
    return max_balls
            
def check_possible(all_game_data, combo):
    """check if combo is possible"""
    sum_game_id = 0
    for i, game in enumerate(all_game_data):
        # check if combo is possible
        if all(game[colour] <= balls for colour, balls in combo.items()):
            print(f'Game {i+1}: Possible')
            sum_game_id += i+1
        else:
            print(f'Game {i+1}: Impossible')
    print(f'Sum of game id: {sum_game_id}')

def check_power(all_game_data):
    """multiply balls for each colour"""
    sum_power = 0
    for game in all_game_data:
        # multiply balls for each colour
        power = 1
        for colour, balls in game.items():
            power *= balls
        sum_power += power
    print(f'Sum of power: {sum_power}')

# main
if __name__ == "__main__":
    # get input data
    data = get_input(day=2)

    # part a
    # parse data
    all_game_data = parse_game_data(data)
    # check all_game_data for possible combinations
    combo = {'red': 12, 'green': 13, 'blue': 14}
    check_possible(all_game_data, combo)

    # part b
    # check power
    check_power(all_game_data)


