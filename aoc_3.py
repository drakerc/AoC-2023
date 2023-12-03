from typing import List
import re


def get_input_lines() -> List[str]:
    with open("input.txt", "r") as f:
        input_lines = f.read().splitlines()
    return input_lines


def process_input_part_1() -> int:
    special_characters = "!@#$%^&*()-+?_=,<>/"

    input_lines = get_input_lines()
    lines_as_single_chars = {}
    possible_parts_positions = {}

    parts_sum = 0

    for line_number, line in enumerate(input_lines):
        indices_object = re.finditer(r'\d+', line)
        indices = [(index.start(), index.end(), index.group(0)) for index in indices_object]
        possible_parts_positions[line_number] = indices  # contains positions of stand-end of possible part numbers

        lines_as_single_chars[line_number] = []
        for character in line:
            lines_as_single_chars[line_number].append(character)

    for line_number, line in possible_parts_positions.items():
        for possible_part_indices in line:
            (possible_part_start, possible_part_end, possible_part_number) = possible_part_indices

            try:
                if lines_as_single_chars[line_number][possible_part_start-1] in special_characters:  # look left
                    parts_sum = parts_sum + int(possible_part_number)
                    continue
            except Exception:
                pass

            try:
                if lines_as_single_chars[line_number][possible_part_end] in special_characters:  # look right
                    parts_sum = parts_sum + int(possible_part_number)
                    continue
            except Exception:
                pass

            for i in range(possible_part_start-1, possible_part_end+1):
                try:
                    if lines_as_single_chars[line_number-1][i] in special_characters:  # look up
                        parts_sum = parts_sum + int(possible_part_number)
                        break
                except Exception:
                    pass

                try:
                    if lines_as_single_chars[line_number+1][i] in special_characters:  # look down
                        parts_sum = parts_sum + int(possible_part_number)
                        break
                except Exception:
                    pass

    return parts_sum


def find_number(possible_parts_positions, selected_line_number, selected_gear_position):
    for possible_parts_position in possible_parts_positions[selected_line_number]:
        (possible_part_start, possible_part_end, possible_part_number) = possible_parts_position
        if possible_part_start <= selected_gear_position <= possible_part_end:
            return possible_part_number


def process_input_part_2():
    input_lines = get_input_lines()
    lines_as_single_chars = {}
    possible_parts_positions = {}
    possible_gear_positions = {}

    gears_sum = 0

    for line_number, line in enumerate(input_lines):
        indices_object = re.finditer(r'\d+', line)
        indices = [(index.start(), index.end(), index.group(0)) for index in indices_object]
        possible_parts_positions[line_number] = indices  # contains positions of start-end of possible part numbers

        possible_gear_positions[line_number] = [m.start() for m in re.finditer('\*', line)]

        lines_as_single_chars[line_number] = []
        for character in line:
            lines_as_single_chars[line_number].append(character)

    for line_number, possible_gear_positions in possible_gear_positions.items():
        for possible_gear_position in possible_gear_positions:
            try:
                # look for a number to the left
                if lines_as_single_chars[line_number][possible_gear_position-1].isnumeric():  # 333*
                    left_gear_number = find_number(possible_parts_positions, line_number, possible_gear_position-1)
                    # look for a number to the right
                    if lines_as_single_chars[line_number][possible_gear_position+1].isnumeric():  # *333
                        right_gear_number = find_number(possible_parts_positions, line_number, possible_gear_position+1)
                        gears_sum = gears_sum + (int(left_gear_number) * int(right_gear_number))
                        break
                    else:
                        # look up
                        for i in range(possible_gear_position-1, possible_gear_position+1):
                            try:
                                if lines_as_single_chars[line_number-1][i].isnumeric():  # look up
                                    right_gear_number = find_number(possible_parts_positions, line_number-1, i)
                                    gears_sum = gears_sum + (int(left_gear_number) * int(right_gear_number))
                                    break
                            except Exception:
                                pass
                        # look down
                        for i in range(possible_gear_position-1, possible_gear_position+1):
                            try:
                                if lines_as_single_chars[line_number+1][i].isnumeric():  # look up
                                    right_gear_number = find_number(possible_parts_positions, line_number+1, i)
                                    gears_sum = gears_sum + (int(left_gear_number) * int(right_gear_number))
                                    break
                            except Exception:
                                pass

            except Exception:
                pass

            try:
                # look for a number to the right
                if lines_as_single_chars[line_number][possible_gear_position+1].isnumeric():  # *333
                    right_gear_number = find_number(possible_parts_positions, line_number, possible_gear_position+1)
                    # look up
                    for i in range(possible_gear_position-1, possible_gear_position+1):
                        try:
                            if lines_as_single_chars[line_number-1][i].isnumeric():  # look up
                                left_gear_number = find_number(possible_parts_positions, line_number-1, i)
                                gears_sum = gears_sum + (int(left_gear_number) * int(right_gear_number))
                                break
                        except Exception:
                            pass
                    # look down
                    for i in range(possible_gear_position-1, possible_gear_position+1):
                        try:
                            if lines_as_single_chars[line_number+1][i].isnumeric():  # look up
                                right_gear_number = find_number(possible_parts_positions, line_number+1, i)
                                gears_sum = gears_sum + (int(left_gear_number) * int(right_gear_number))
                                break
                        except Exception:
                            pass

            except Exception:
                pass

            try:
                # look for a number up
                for i in range(possible_gear_position-1, possible_gear_position+2):
                    try:
                        if lines_as_single_chars[line_number-1][i].isnumeric():  # look up
                            left_gear_number = find_number(possible_parts_positions, line_number-1, i)
                            break
                    except Exception:
                        pass
                        # look down
                for i in range(possible_gear_position-2, possible_gear_position+1):
                    try:
                        if lines_as_single_chars[line_number+1][i].isnumeric():  # look up
                            right_gear_number = find_number(possible_parts_positions, line_number+1, i)
                            gears_sum = gears_sum + (int(left_gear_number) * int(right_gear_number))
                            break
                    except Exception:
                        pass

            except Exception:
                pass

    return gears_sum

def main():
    print(process_input_part_1())
    print(process_input_part_2())


if __name__ == "__main__":
    main()
