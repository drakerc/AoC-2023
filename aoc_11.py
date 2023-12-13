from typing import List


def get_input_lines() -> List[str]:
    with open("input.txt", "r") as f:
        input_lines = f.read().splitlines()
    return input_lines


def process_input_part_1() -> int:
    input_lines = get_input_lines()
    total_shortest_paths = 0

    image_map = []

    doubled_horizontal_lines = []
    doubled_vertical_lines = []

    line_length = None

    for i, v in enumerate(input_lines):
        image_map.append([c for c in v])
        if not line_length:
            line_length = len(v)
        if all([pos == "." for pos in v]):
            doubled_horizontal_lines.append(i)

    for i in range(0, line_length):
        for index, value in enumerate(image_map):
            if value[i] != ".":
                break
            if index == len(image_map)-1:
                doubled_vertical_lines.append(i)

    for i, doubled_horizontal_line in enumerate(doubled_horizontal_lines):
        image_map.insert(doubled_horizontal_line+1 + i, ["." for i in range(0, line_length)])

    for i, doubled_vertical_line in enumerate(doubled_vertical_lines):
        for item in image_map:
            item.insert(doubled_vertical_line + 1 + i, ".")

    galaxy_coordinates = []

    for x, v_list in enumerate(image_map):
        for y, v in enumerate(v_list):
            if v == "#":
                galaxy_coordinates.append((x, y))

    for galaxy_number, galaxy_coordinate in enumerate(galaxy_coordinates):
        coord_x, coord_y = galaxy_coordinate
        for next_galaxy in galaxy_coordinates[galaxy_number+1:]:
            next_galaxy_coord_x, next_galaxy_coord_y = next_galaxy
            shortest_path = abs((next_galaxy_coord_x - coord_x)) + abs((next_galaxy_coord_y - coord_y))
            total_shortest_paths += shortest_path
    return total_shortest_paths


def main():
    print(process_input_part_1())


if __name__ == "__main__":
    main()
