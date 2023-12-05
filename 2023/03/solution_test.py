"""
Advent of Code: Day 03, 2023
Name: Gear Ratios
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


@pytest.mark.parametrize("index, expected", [(0, {"is_number": True, "is_symbol": False, "text": "467", "x_start": 0, "x_end": 2, "y": 0})])
def test_parse_data_example_1(example_1, index, expected):
    assert example_1[0] == expected

@pytest.mark.parametrize(
        "entity_1, entity_2, expected",
        [
            (
                {"is_number": True, "is_symbol": False, "text": "467", "x_start": 0, "x_end": 2, "y": 0},
                {"is_number": False, "is_symbol": True, "text": ":", "x_start": 3, "x_end": 3, "y": 0},
                True                
            ),
            (
                {"is_number": True, "is_symbol": False, "text": "467", "x_start": 0, "x_end": 2, "y": 0},
                {"is_number": True, "is_symbol": False, "text": "2", "x_start": 4, "x_end": 4, "y": 0},
                False
            ),
            (
                {"is_number": True, "is_symbol": False, "text": "467", "x_start": 0, "x_end": 2, "y": 0},
                {"is_number": False, "is_symbol": True, "text": ":", "x_start": 3, "x_end": 3, "y": 2},
                False
            )
        ]
    )
def test_entities_are_adjacent_example_1(entity_1, entity_2, expected):
    assert solution.entities_are_adjacent(entity_1, entity_2) == expected


@pytest.mark.parametrize(
    "entity, expected",
    [
        (
            {"is_number": True, "is_symbol": False, "text": "467", "x_start": 0, "x_end": 2, "y": 0},
            {"is_number": False, "is_symbol": True, "text": "*", "x_start": 3, "x_end": 3, "y": 1}
        )
    ]
)
def test_get_adjacent_entities_example_1(example_1, entity, expected):
    adjacent_entities = solution.get_adjacent_entities(entity, example_1)
    assert len(adjacent_entities) == 1
    assert adjacent_entities[0] == expected

def test_get_part_numbers_example_1(example_1):
    part_numbers = solution.get_part_numbers(example_1)
    assert part_numbers[0] == {"is_number": True, "is_symbol": False, "text": "467", "x_start": 0, "x_end": 2, "y": 0}
    assert part_numbers[1]["text"] == "35"
    assert "114" not in [part_number["text"] for part_number in part_numbers]

def test_part_1_example_1(example_1):
    assert solution.part_1(example_1) == 4361

def test_get_gear(example_1):
    gears = solution.get_gears(example_1)
    assert gears[0]["gear"] == {"is_number": False, "is_symbol": True, "text": "*", "x_start": 3, "x_end": 3, "y": 1}
    assert gears[0]["part_numbers"][0] == {"is_number": True, "is_symbol": False, "text": "467", "x_start": 0, "x_end": 2, "y": 0}
    assert gears[0]["part_numbers"][1] == {"is_number": True, "is_symbol": False, "text": "35", "x_start": 2, "x_end": 3, "y": 2}
    assert len(gears) == 2

def test_get_gear_ratio(example_1):
    gears = solution.get_gears(example_1)
    assert solution.get_gear_ratio(gears[0]) == 16345
    assert solution.get_gear_ratio(gears[1]) == 451490

def test_part_2_example_1(example_1):
    assert solution.part_2(example_1) == 467835