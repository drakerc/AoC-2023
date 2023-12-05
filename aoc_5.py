import multiprocessing
import time
from collections import defaultdict
from multiprocessing import Process, Pool
from typing import List
import re


def get_input_lines() -> List[str]:
    with open("input.txt", "r") as f:
        input_lines = f.read().splitlines()
    return input_lines


def process_input_part_1() -> int:
    input_lines = get_input_lines()

    seeds = []
    seeds_mapping_in_order = defaultdict(list)
    mapping_locations = [
        "seed-to-soil map:",
        "soil-to-fertilizer map:",
        "fertilizer-to-water map:",
        "water-to-light map:",
        "light-to-temperature map:",
        "temperature-to-humidity map:",
        "humidity-to-location map:"
    ]
    mapping_location = -1

    for input_line in input_lines:
        if input_line.startswith("seeds: "):
            seeds_input = input_line.split()
            seeds = [int(seed) for seed in seeds_input[1:]]
            continue
        if input_line in mapping_locations:
            mapping_location = mapping_location + 1
            continue
        if input_line and input_line[0].isnumeric():
            mapping_list = input_line.split()
            destination = int(mapping_list[0])
            range_start = int(mapping_list[1])
            range_length = int(mapping_list[2])
            range_end = range_start + range_length - 1
            seeds_mapping_in_order[mapping_location].append({
                "range_start": range_start,
                "range_end": range_end,
                "destination": destination
            })

    seed_locations = []

    for seed in seeds:
        seed_destination = seed
        for mapping_element in seeds_mapping_in_order.values():  # mapping_element = e.g. seed-to-soil range
            for mapping_range_dict in mapping_element:
                if mapping_range_dict["range_start"] <= seed_destination <= mapping_range_dict["range_end"]:
                    seed_destination = seed_destination - mapping_range_dict["range_start"] + mapping_range_dict["destination"]
                    break
        seed_locations.append(seed_destination)

    return min(seed_locations)


def calculate_minimum(argus):
    (seed_range_start, seed_range_end, seeds_mapping_in_order) = argus
    print(f"new process {seed_range_start}")
    minimum_seed_location = None
    total_to_process = len(range(seed_range_start, seed_range_start + seed_range_end - 1))
    next_progress_to_display = 0.1
    print("test")
    for i, seed in enumerate(range(seed_range_start, seed_range_start + seed_range_end - 1)):
        progress = (i / total_to_process) * 100
        if progress > next_progress_to_display:
            next_progress_to_display = next_progress_to_display + 0.1
            print(progress)
        seed_destination = seed
        for mapping_element in seeds_mapping_in_order.values():  # mapping_element = e.g. seed-to-soil range
            for mapping_range_dict in mapping_element:
                if mapping_range_dict["range_start"] <= seed_destination <= mapping_range_dict["range_end"]:
                    seed_destination = seed_destination - mapping_range_dict["range_start"] + mapping_range_dict["destination"]
                    break
        if not minimum_seed_location or seed_destination < minimum_seed_location:
            minimum_seed_location = seed_destination

    print(minimum_seed_location)
    return minimum_seed_location


def process_input_part_2() -> int:
    input_lines = get_input_lines()

    seeds_mapping_in_order = defaultdict(list)
    mapping_locations = [
        "seed-to-soil map:",
        "soil-to-fertilizer map:",
        "fertilizer-to-water map:",
        "water-to-light map:",
        "light-to-temperature map:",
        "temperature-to-humidity map:",
        "humidity-to-location map:"
    ]
    mapping_location = -1

    for input_line in input_lines:
        if input_line.startswith("seeds: "):
            seeds_input = input_line.split()[1:]
        if input_line in mapping_locations:
            mapping_location = mapping_location + 1
            continue
        if input_line and input_line[0].isnumeric():
            mapping_list = input_line.split()
            destination = int(mapping_list[0])
            range_start = int(mapping_list[1])
            range_length = int(mapping_list[2])
            range_end = range_start + range_length - 1
            seeds_mapping_in_order[mapping_location].append({
                "range_start": range_start,
                "range_end": range_end,
                "destination": destination
            })

    processes = []

    seed_range_start = None
    seed_range_end = None

    seed_ranges = []
    
    for seed in seeds_input:
        seed = int(seed)
        if not seed_range_start:
            seed_range_start = seed
            continue
        if not seed_range_end:
            seed_range_end = seed
        if seed_range_start and seed_range_end:
            seed_ranges.append([seed_range_start, seed_range_end, seeds_mapping_in_order])
            seed_range_start = None
            seed_range_end = None
            continue

    seed_ranges = tuple(seed_ranges)
    pool_r = Pool(len(seed_ranges))

    return min(pool_r.map(calculate_minimum, seed_ranges))


def main():
    print(process_input_part_1())
    print(process_input_part_2())


if __name__ == "__main__":
    main()
