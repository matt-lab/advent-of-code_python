"""
Advent of Code: Day 04, 2023
Name: Scratchcards
"""

# Standard library imports
from pathlib import Path
# Third party imports
import pytest
# Local imports
import solution

# Constants
PUZZLE_DIR = Path(__file__).parent

# Tests for each example
@pytest.fixture
def example_1():
    puzzle_input = (PUZZLE_DIR / "example_1.txt").read_text()
    return solution.parse_data(puzzle_input)

@pytest.mark.parametrize(
    "winning_numbers, card_numbers, expected",
    [
        ([1, 2, 3], [1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [1, 2, 4], [1, 2]),
        ([1, 2, 3], [4, 5, 6], [])
    ]
)
def test_get_winning_card_numbers(winning_numbers, card_numbers, expected):
    assert solution.get_winning_card_numbers(winning_numbers, card_numbers) == expected

@pytest.mark.parametrize(
    "winning_card_numbers, expected",
    [
        ([48, 83, 17, 86], 8),
        ([32, 61], 2),
        ([1, 21], 2),
        ([84], 1),
        ([], 0)
    ]
)
def test_get_points(winning_card_numbers, expected):
    assert solution.get_points(winning_card_numbers) == expected


def test_part_1_example_1(example_1):
    assert solution.part_1(example_1) == 13

def test_part_2_example_1(example_1):
    assert solution.part_2(example_1) == 30
