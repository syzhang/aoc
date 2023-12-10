"""
day 5
"""
import re
from functools import reduce
from utils import get_input
from tqdm import tqdm
from math import ceil, log10


def extract_seeds(data):
    """extract seeds from input"""
    # split every other line
    seeds, *mappings = data.split("\n\n")
    # extract seeds and convert to int
    seeds = list(map(int, seeds.split()[1:]))
    # print(seeds)
    return seeds, *mappings


def extract_mappings(start, mapping):
    """extract mappings from input"""
    for m in mapping.split("\n")[1:]:
        # extract data
        if not m:
            continue
        destination, source, range_len = m.split()
        # convert to int
        destination = int(destination)
        source = int(source)
        range_len = int(range_len)
        # find offset
        delta = start - source
        if delta in range(range_len):
            return destination + delta
    else:
        return start


def find_mapping(seeds, mapping):
    """find mapping to final"""
    locations = []
    for start in seeds:
        location = reduce(extract_mappings, mapping, start)
        locations.append(location)
    return locations


def brute_force_mapping(seeds, mapping, print_output=True):
    """find mapping to final"""
    new_seeds = []
    seed_start = seeds[0::2]
    seed_range = seeds[1::2]
    
    # Calculate step size
    max_seed = max(seed_range)
    step_size = int(pow(10, ceil(log10(max_seed / 100))))
    
    # Generate search values
    search_vals = generate_search_values(zip(seed_start, seed_range), step_size, mapping)
    
    # Get rough estimate
    rough_est = min(search_vals.items(), key = lambda x: x[1])
    seed_range_start, seed_range_end, best_est = rough_est[0]

    print(f'Best estimate: {best_est} in seed range {seed_range_start} to {seed_range_end}')
    print(f'Step size: {step_size:<8d}, best estimate: {best_est:<10d} near location {rough_est[1]}')

    while step_size > 1:
        left_search  = max(best_est - step_size, seed_range_start)
        right_search = min(best_est + step_size, seed_range_end)

        step_size = step_size // 10
        search_vals = {s: find_mapping([s], mapping=mapping) for s in range(left_search, right_search, step_size)}
        best_est, best_loc = min(search_vals.items(), key = lambda x: x[1])

        if print_output:
            print(f'Step size: {step_size:<8d}, best estimate: {best_est:<10d} near loc {best_loc}')

    return best_loc

def generate_search_values(seeds, step_size, mapping):
    """Generate search values using seeds, step size and maps"""
    search_vals = {}
    for ss, sl in seeds:
        for s in range(ss, ss + sl, step_size):
            search_vals[(ss, ss + sl, s)] = find_mapping(seeds=[s], mapping=mapping)
    return search_vals


# main
if __name__ == "__main__":
    # get input data
    # input_data = get_input(day=5, test_data=True)
    input_data = get_input(day=5, test_data=False)

    # solve
    # part a
    seeds, *mappings = extract_seeds(input_data)
    # find location
    # locations = find_mapping(seeds, mappings)
    # print(min(locations))

    # part b
    min_loc = brute_force_mapping(seeds, mappings)
    print(min_loc)
