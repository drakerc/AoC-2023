from collections import defaultdict
from typing import List


def get_input_lines() -> List[str]:
    with open("input.txt", "r") as f:
        input_lines = f.read().splitlines()
    return input_lines


def process_input_part_1() -> int:
    input_lines = get_input_lines()

    differences = defaultdict(list)
    total_sum = 0

    for input_line_index, input_line_value in enumerate(input_lines):
        input_values = [int(v) for v in input_line_value.split()]

        differences[0] = input_values

        current_difference_index = 1
        differences[current_difference_index] = []
        for index, input_value in enumerate(input_values):
            try:
                differences[current_difference_index].append(input_values[index+1] - input_value)
            except Exception:
                continue

        while True:
            difference_values = differences[current_difference_index]
            if all(node == 0 for node in difference_values):
                total_sum += sum([x[-1] for x in differences.values()])
                break
            differences[current_difference_index+1] = []

            i = 0
            while (i < len(difference_values) - 1):
                differences[current_difference_index+1].append(difference_values[i+1] - difference_values[i])
                i += 1
            current_difference_index += 1

    return total_sum


def main():
    print(process_input_part_1())


if __name__ == "__main__":
    main()
