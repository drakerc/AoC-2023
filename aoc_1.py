from typing import List

NUMBER_TO_WORD_MAPPING = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def get_input_lines() -> List[str]:
    with open("input.txt", "r") as f:
        input_lines = f.readlines()
    return input_lines


def process_input() -> int:
    input_lines = get_input_lines()
    sum_of_numbers = 0
    for line in input_lines:
        words_and_numbers = list(NUMBER_TO_WORD_MAPPING.keys()) + list(NUMBER_TO_WORD_MAPPING.values())
        found_numbers = {}
        for v in words_and_numbers:
            found_numbers = {**found_numbers, **{i: v for i in range(len(line)) if line.startswith(v, i)}}

        sorted_list = sorted(found_numbers.items())
        first_number = sorted_list[0][1] if len(sorted_list[0][1]) == 1 else NUMBER_TO_WORD_MAPPING[sorted_list[0][1]]
        last_number = sorted_list[-1][1] if len(sorted_list[-1][1]) == 1 else NUMBER_TO_WORD_MAPPING[sorted_list[-1][1]]
        whole_number = int(f"{first_number}{last_number}")

        sum_of_numbers = sum_of_numbers + whole_number
    return sum_of_numbers


def main():
    print(process_input())


if __name__ == "__main__":
    main()
