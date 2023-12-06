import multiprocessing
import time
from collections import defaultdict
from functools import reduce
from multiprocessing import Process
from typing import List
import re


def get_input_lines() -> List[str]:
    with open("input.txt", "r") as f:
        input_lines = f.read().splitlines()
    return input_lines


def process_input_part_1() -> int:
    input_lines = get_input_lines()

    time_line = input_lines[0]
    distance_line = input_lines[1]
    possible_solutions = defaultdict(int)

    possible_times = [int(time_line) for time_line in time_line.split()[1:]]
    distances = [int(distance_line) for distance_line in distance_line.split()[1:]]

    for index, max_time in enumerate(possible_times):
        min_distance = distances[index]

        for charging_time in range(1, max_time):
            remaining_time = max_time - charging_time
            traveled_distance = charging_time * remaining_time
            if traveled_distance > min_distance:
                possible_solutions[index] = possible_solutions[index] + 1

    return reduce(lambda x, y: x*y, possible_solutions.values())


def process_input_part_2() -> int:
    input_lines = get_input_lines()

    time_line = input_lines[0].split(":")[1].replace(" ", "")
    distance_line = input_lines[1].split(":")[1].replace(" ", "")
    possible_solutions = defaultdict(int)

    possible_times = [int(time_line) for time_line in [time_line]]
    distances = [int(distance_line) for distance_line in [distance_line]]

    for index, max_time in enumerate(possible_times):
        min_distance = distances[index]

        for charging_time in range(1, max_time):
            # print(f"{charging_time}, max={max_time}")
            remaining_time = max_time - charging_time
            traveled_distance = charging_time * remaining_time
            if traveled_distance > min_distance:
                possible_solutions[index] = possible_solutions[index] + 1

    return reduce(lambda x, y: x*y, possible_solutions.values())


def main():
    print(process_input_part_1())
    print(process_input_part_2())


if __name__ == "__main__":
    main()
