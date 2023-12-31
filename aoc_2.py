from typing import List


def get_input_lines() -> List[str]:
    with open("input.txt", "r") as f:
        input_lines = f.readlines()
    return input_lines


def process_input() -> int:
    maximum_colors = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    sum_of_game_ids = 0
    input_lines = get_input_lines()

    for line in input_lines:
        split_by_game_id = line.split(":")
        game_id = split_by_game_id[0].split()[-1]
        games = split_by_game_id[1].split(";")
        impossible = False
        for game in games:
            split_by_colors = game.split(",")
            for split_by_color in split_by_colors:
                split_by_numbers_and_colors = split_by_color.split()
                if int(split_by_numbers_and_colors[0]) > maximum_colors[split_by_numbers_and_colors[1]]:
                    impossible = True
                    break
        if not impossible:
            sum_of_game_ids = sum_of_game_ids + int(game_id)
    return sum_of_game_ids


def process_input_part_2() -> int:
    input_lines = get_input_lines()
    power_of_colors = 0

    for line in input_lines:
        minimum_colors = {
            "red": 1,
            "green": 1,
            "blue": 1
        }
        split_by_game_id = line.split(":")
        games = split_by_game_id[1].split(";")
        for game in games:
            split_by_colors = game.split(",")
            for split_by_color in split_by_colors:
                split_by_numbers_and_colors = split_by_color.split()
                if int(split_by_numbers_and_colors[0]) > minimum_colors[split_by_numbers_and_colors[1]]:
                    minimum_colors[split_by_numbers_and_colors[1]] = int(split_by_numbers_and_colors[0])
        power_of_color = minimum_colors["red"] * minimum_colors["green"] * minimum_colors["blue"]
        power_of_colors = power_of_colors + power_of_color
    return power_of_colors


def main():
    print(process_input())
    print(process_input_part_2())


if __name__ == "__main__":
    main()
