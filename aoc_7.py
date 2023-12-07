from collections import Counter
from typing import List


def get_input_lines() -> List[str]:
    with open("input.txt", "r") as f:
        input_lines = f.read().splitlines()
    return input_lines


def process_input_part_1() -> int:
    input_lines = get_input_lines()

    mapped_hands = {
        "high_card": [],
        "one_pair": [],
        "two_pair": [],
        "three_of_a_kind": [],
        "full_house": [],
        "four_of_a_kind": [],
        "five_of_a_kind": [],
    }

    hands_and_bids = {}

    sorting_order = "AKQJT98765432"

    for line in input_lines:
        hand, bid = line.split()
        hands_and_bids[hand] = int(bid)
        counted_chars = Counter(hand).most_common()

        if counted_chars[0][1] == 5:
            mapped_hands["five_of_a_kind"].append(hand)
            continue
        elif counted_chars[0][1] == 4:
            mapped_hands["four_of_a_kind"].append(hand)
            continue
        elif counted_chars[0][1] == 3 and counted_chars[1][1] == 2:
            mapped_hands["full_house"].append(hand)
            continue
        elif counted_chars[0][1] == 3 and counted_chars[1][1] == 1:
            mapped_hands["three_of_a_kind"].append(hand)
            continue
        elif counted_chars[0][1] == 2 and counted_chars[1][1] == 2:
            mapped_hands["two_pair"].append(hand)
            continue
        elif counted_chars[0][1] == 2:
            mapped_hands["one_pair"].append(hand)
            continue
        else:
            mapped_hands["high_card"].append(hand)
            continue

    rank_counter = 1
    bids = 0

    for index, value in mapped_hands.items():
        mapped_hands[index] = sorted(value, key=lambda word: [sorting_order.index(c) for c in word], reverse=True)
        for card in mapped_hands[index]:
            bids += hands_and_bids[card] * rank_counter
            rank_counter += 1

    return bids


def process_input_part_2() -> int:
    input_lines = get_input_lines()

    mapped_hands = {
        "high_card": [],
        "one_pair": [],
        "two_pair": [],
        "three_of_a_kind": [],
        "full_house": [],
        "four_of_a_kind": [],
        "five_of_a_kind": [],
    }

    hands_and_bids = {}

    sorting_order = "AKQT98765432J"

    for line in input_lines:
        hand, bid = line.split()
        hands_and_bids[hand] = int(bid)
        counter_chars = Counter(hand)
        jokers_count = counter_chars.get("J")
        counted_chars = counter_chars.most_common()
        counted_chars_without_joker = [card[1] for card in counted_chars if card[0] != "J"]

        if (jokers_count == 5) or (jokers_count and counted_chars_without_joker[0] == 5 - jokers_count) or \
                counted_chars_without_joker[0] == 5:
            mapped_hands["five_of_a_kind"].append(hand)
            continue
        elif (jokers_count and counted_chars_without_joker[0] == 4 - jokers_count) or counted_chars_without_joker[
            0] == 4:
            mapped_hands["four_of_a_kind"].append(hand)
            continue
        elif (jokers_count and counted_chars_without_joker[0] == 3 - jokers_count and counted_chars_without_joker[
            1] == 2) or (counted_chars_without_joker[0] == 3 and counted_chars_without_joker[1] == 2):
            mapped_hands["full_house"].append(hand)
            continue
        elif (jokers_count and counted_chars_without_joker[0] == 3 - jokers_count and counted_chars_without_joker[
            1] == 1) or (counted_chars_without_joker[0] == 3 and counted_chars_without_joker[1] == 1):
            mapped_hands["three_of_a_kind"].append(hand)
            continue
        elif (jokers_count and counted_chars_without_joker[0] == 2 - jokers_count and counted_chars_without_joker[
            1] == 2) or (counted_chars_without_joker[0] == 2 and counted_chars_without_joker[1] == 2):
            mapped_hands["two_pair"].append(hand)
            continue
        elif (jokers_count and counted_chars_without_joker[0] == 2 - jokers_count) or counted_chars_without_joker[
            0] == 2:
            mapped_hands["one_pair"].append(hand)
            continue
        else:
            mapped_hands["high_card"].append(hand)
            continue

    rank_counter = 1
    bids = 0

    for index, value in mapped_hands.items():
        mapped_hands[index] = sorted(value, key=lambda word: [sorting_order.index(c) for c in word], reverse=True)
        for card in mapped_hands[index]:
            bids += hands_and_bids[card] * rank_counter
            rank_counter += 1

    return bids


def main():
    print(process_input_part_1())
    print(process_input_part_2())


if __name__ == "__main__":
    main()
