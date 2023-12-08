"""
day 5
"""
import re
from functools import reduce
from utils import get_input
from tqdm import tqdm


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


def brute_force_mapping(seeds, mapping):
    """find mapping to final"""
    new_seeds = []
    seed_start = seeds[0::2]
    seed_range = seeds[1::2]
    min_loc = int(1e100)
    min_seed = 0
    min_range = 0
    for start, seed_range in tqdm(zip(seed_start, seed_range)):
        # check every sqrt of seed_range
        n_steps = (start + seed_range) // 2
        for i in range(start, start + seed_range, n_steps):
            location = reduce(extract_mappings, mapping, i)
            if location < min_loc:
                min_loc = location
                min_seed = i
                min_range = seed_range

    # iterate over range of min_seed
    for i in tqdm(range(min_seed, min_seed + min_range)):
        location = reduce(extract_mappings, mapping, i)
        if location < min_loc:
            min_loc = location
    return min_loc


def extract_mappings_b(inputs, mapping):
    """extract mappings from input"""
    for start, seed_range in inputs:
        while seed_range > 0:
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
                    range_len = min(range_len - delta, seed_range)
                    yield (destination + delta, range_len)
                    start += range_len
                    seed_range -= range_len
                    break
            else:
                return (start, range_len)


def find_mapping_b(seeds, mapping):
    """find mapping to final"""
    seed_start = seeds[0::2]
    seed_range = seeds[1::2]
    pairs = zip(seed_start, seed_range)
    locations = []
    for s in pairs:
        locs = list(reduce(extract_mappings_b, mapping, [s]))  # get a list of mappings
        if locs:  # check if locs is not empty
            min_loc = min(locs)
            locations.append(min_loc[0])
    return locations


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
    # locations = find_mapping_b(seeds, mappings)
    min_loc = brute_force_mapping(seeds, mappings)
    print(min_loc)
