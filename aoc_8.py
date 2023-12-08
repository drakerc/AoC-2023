from typing import List


def get_input_lines() -> List[str]:
    with open("input.txt", "r") as f:
        input_lines = f.read().splitlines()
    return input_lines


def process_input_part_1() -> int:
    input_lines = get_input_lines()

    first_node = "AAA"
    final_node = "ZZZ"

    instructions = input_lines[0]

    node_steps = {}
    steps_taken = 0

    for node in input_lines[2:]:
        node_elements = node.split()
        node_start = node_elements[0]

        left_turn = ''.join(filter(str.isalpha, node_elements[2]))
        right_turn = ''.join(filter(str.isalpha, node_elements[3]))

        node_steps[node_start] = {"left": left_turn, "right": right_turn}

    current_step = 0
    current_node = first_node
    while current_node != final_node:
        try:
            current_step_direction = instructions[current_step]
        except IndexError:
            current_step = 0
            current_step_direction = instructions[current_step]

        if current_step_direction == "L":
            current_node = node_steps[current_node]["left"]
        if current_step_direction == "R":
            current_node = node_steps[current_node]["right"]
        steps_taken = steps_taken + 1
        current_step = current_step + 1
        continue

    return steps_taken


def main():
    print(process_input_part_1())


if __name__ == "__main__":
    main()
