from collections import defaultdict
from typing import List
import re


def get_input_lines() -> List[str]:
    with open("input.txt", "r") as f:
        input_lines = f.read().splitlines()
    return input_lines


def process_input_part_1() -> int:
    input_lines = get_input_lines()
    total_won_points = 0

    for input_line in input_lines:
        winning_numbers_str, own_numbers_str = input_line.split("|")
        winning_numbers = winning_numbers_str.split()[2:]  # ignore Card X str
        own_numbers = own_numbers_str.split()

        won_numbers = list(set(own_numbers) & set(winning_numbers))
        if won_numbers:
            won_points = pow(2, len(won_numbers) - 1)
            total_won_points = total_won_points + won_points

    return total_won_points


def process_input_part_2() -> int:
    input_lines = get_input_lines()
    won_cards_by_card_id = defaultdict(int)
    owned_cards = defaultdict(int)

    for input_line in input_lines:
        winning_numbers_str, own_numbers_str = input_line.split("|")
        winning_id_and_numbers = winning_numbers_str.split()[1:]  # ignore Card X str
        winning_id = int(winning_id_and_numbers[0][:-1])
        winning_numbers = winning_id_and_numbers[1:]
        own_numbers = own_numbers_str.split()

        owned_cards[winning_id] += 1

        won_numbers = list(set(own_numbers) & set(winning_numbers))
        # Processing original cards
        won_amount = len(won_numbers)
        won_cards_by_card_id[winning_id] = won_amount

        for i in range(winning_id+1, int(winning_id) + won_amount + 1):
            owned_cards[i] += 1

    # processing copies
    for owned_card_id, owned_card_copies in owned_cards.items():
        if owned_card_copies < 2:
            continue
        amount_of_copies = owned_card_copies-1
        how_many_wins = won_cards_by_card_id[owned_card_id]
        for i in range(owned_card_id+1, int(owned_card_id) + how_many_wins + 1):
            owned_cards[i] += amount_of_copies * 1

    return sum(owned_cards.values())


def main():
    print(process_input_part_1())
    print(process_input_part_2())


if __name__ == "__main__":
    main()
