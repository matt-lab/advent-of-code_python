"""
Advent of Code: Day 04, 2023
Name: Scratchcards
"""

# Standard library imports
from pathlib import Path
import re

def parse_data(puzzle_input):
    """Parse input."""
    pattern = r"^Card\s+(?P<id>\d+):(?P<winning_numbers>[\d\s]*)\|(?P<card_numbers>[\d\s]*)$"
    lines = puzzle_input.splitlines()
    cards = []
    for line in lines:
        match = re.match(pattern, line)
        card = match.groupdict()
        card['id'] = int(card['id'])
        card['winning_numbers'] = list(map(int, re.findall(r'\d+', card['winning_numbers'])))
        card['card_numbers'] = list(map(int, re.findall(r'\d+', card['card_numbers'])))
        cards.append(card)
    return cards

def get_winning_card_numbers(winning_numbers, card_numbers):
    return list(set(card_numbers).intersection(set(winning_numbers)))

def get_points(winning_card_numbers):
    if len(winning_card_numbers) == 0:
        return 0
    return 2 ** (len(winning_card_numbers) - 1)

def part_1(data):
    """Solve part 1."""
    points = 0
    for card in data:
        winning_card_numbers = get_winning_card_numbers(card['winning_numbers'], card['card_numbers'])
        points += get_points(winning_card_numbers)
    return points


def ids_to_duplicate(id, n):
    return [n for n in range(id + 1, id + n + 1)]


def part_2(data):
    """Solve part 2."""
    cards = data
    counts = [1 for card in cards]
    for card in cards:
        id = card['id']
        count = counts[id - 1]
        winning_card_numbers = get_winning_card_numbers(card['winning_numbers'], card['card_numbers'])
        new_cards = ids_to_duplicate(id, len(winning_card_numbers))
        for new_card in new_cards:
            counts[new_card - 1] += count
    return sum(counts)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part_1(data)
    yield part_2(data)


if __name__ == "__main__":
    puzzle_path = Path(__file__).parent
    input_path = puzzle_path / "input.txt"
    solutions = solve(puzzle_input = Path(input_path).read_text())
    for index, solution in enumerate(solutions, start = 1):
        solution_path = puzzle_path / f"solution_{index}.txt"
        solution_path.write_text(str(solution))