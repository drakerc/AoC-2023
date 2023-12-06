from collections import defaultdict
from functools import reduce
from typing import List


def get_input_lines() -> List[str]:
    with open("input.txt", "r") as f:
        input_lines = f.read().splitlines()
    return input_lines


def do_calculations(max_times: List[int], min_distances: List[int]):
    possible_solutions = defaultdict(int)

    for index, max_time in enumerate(max_times):
        min_distance = min_distances[index]

        for charging_time in range(1, max_time):
            remaining_time = max_time - charging_time
            traveled_distance = charging_time * remaining_time
            if traveled_distance > min_distance:
                possible_solutions[index] = possible_solutions[index] + 1

    return reduce(lambda x, y: x*y, possible_solutions.values())


def process_input_part_1() -> int:
    input_lines = get_input_lines()

    max_times = [int(time_line) for time_line in input_lines[0].split()[1:]]
    min_distances = [int(distance_line) for distance_line in input_lines[1].split()[1:]]

    return do_calculations(max_times, min_distances)


def process_input_part_2() -> int:
    input_lines = get_input_lines()

    # there will be just one element in there, but this can help with reusing the calculations function
    max_times = [int(input_lines[0].split(":")[1].replace(" ", ""))]
    min_distances = [int(input_lines[1].split(":")[1].replace(" ", ""))]

    return do_calculations(max_times, min_distances)


def main():
    print(process_input_part_1())
    print(process_input_part_2())


if __name__ == "__main__":
    main()
