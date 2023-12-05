import time
from collections import defaultdict
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


def process_input_part_2() -> int:
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

    seed_locations = []

    minimum_seed_location = None

    seed_range_start = None
    seed_range_end = None
    for seed in seeds_input:
        seed = int(seed)
        if not seed_range_start:
            seed_range_start = seed
            continue
        if not seed_range_end:
            seed_range_end = seed
        if seed_range_start and seed_range_end:
            print("new range")
            for seed in range(seed_range_start, seed_range_start + seed_range_end - 1):
                seed_destination = seed
                for mapping_element in seeds_mapping_in_order.values():  # mapping_element = e.g. seed-to-soil range
                    for mapping_range_dict in mapping_element:
                        if mapping_range_dict["range_start"] <= seed_destination <= mapping_range_dict["range_end"]:
                            seed_destination = seed_destination - mapping_range_dict["range_start"] + mapping_range_dict["destination"]
                            break
                if not minimum_seed_location or seed_destination < minimum_seed_location:
                    minimum_seed_location = seed_destination
            seed_range_start = None
            seed_range_end = None
            continue

    return minimum_seed_location


def main():
    print(process_input_part_1())
    print(process_input_part_2())


if __name__ == "__main__":
    main()
