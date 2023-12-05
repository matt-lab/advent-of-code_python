"""
Advent of Code: Day 02, 2023
Name: Cube Conundrum
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
        "index,expected",
        [
            (0, {
                    'id' : 1,
                    'subsets': [
                        [{'blue': 3}, {'red': 4}],
                        [{'red': 1}, {'green': 2}, {'blue': 6}],
                        [{'green': 2}]
                    ]
                })
        ])
def test_parse_example_1(example_1, index, expected):
    """Test that input is parsed properly."""
    assert example_1[index] == expected


@pytest.mark.parametrize(
        "subsets,expected",
        [
            ([[{'red': 13}]], False),
            ([[{'red': 12}]], True),
            ([[{'red': 0}]], True),
        ]
)
def test_is_valid_game(subsets, expected):
    """Test that game is valid."""
    assert solution.is_valid_game(subsets) == expected

def test_get_valid_ids(example_1):
    """Test that valid ids are returned."""
    assert solution.get_valid_ids(example_1) == [1, 2, 5]

def test_part_1_example_1(example_1):
    """Test that part 1 is solved."""
    assert solution.part_1(example_1) == 8

@pytest.mark.parametrize(
        "subsets,expected",
        [
            (
                [
                    [{'blue': 3}, {'red': 4}],
                    [{'red': 1}, {'green': 2}, {'blue': 6}],
                    [{'green': 2}]
                ],
                {'red': 4, 'green': 2, 'blue': 6}
            )
        ]
)
def test_get_min_cubes(subsets, expected):
    """Test that minimum number of cubes is returned."""
    assert solution.get_min_cubes(subsets) == expected

def test_part_2_example_1(example_1):
    """Test that part 2 is solved."""
    assert solution.part_2(example_1) == 2286