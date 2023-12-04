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

@pytest.fixture
def example_2():
    puzzle_input = (PUZZLE_DIR / "example_2.txt").read_text()
    return solution.parse_data(puzzle_input)


def test_parse_example_1(example_1):
    """Test that input is parsed properly."""
    assert example_1[0] == "1abc2"

def test_get_ints_from_line(example_1):
    """Test that ints are extracted properly."""
    assert solution.get_ints_from_line(example_1[0]) == [1, 2]

def test_get_calibration_value_from_ints(example_1):
    """Test that calibration value is extracted properly."""
    ints = solution.get_ints_from_line(example_1[0])
    assert solution.get_calibration_value_from_ints(ints) == 12

def test_part_1(example_1):
    """Test that part 1 is solved."""
    assert solution.part_1(example_1) == 142

def test_get_int_words():
    """Test that int words are extracted properly."""
    assert solution.get_int_words() == {
                                    "one": 1, "two": 2, "three": 3,
                                    "four": 4, "five": 5, "six": 6,
                                    "seven": 7, "eight": 8, "nine": 9
                                    }

# @pytest.mark.parametrize(
#     "input,expected",
#     [
#         ("two1nine", "219"),
#         ("4nineeightseven2", "49872"),
#         ("abcone2threexyz", "abc123xyz"),
#         ("33", "33"),
#         ("279four", "2794"),
#         ("eightwothree", "8wo3"),
#         ("xtwone3four", "x2ne34"),
#         ("4nineeightseven2", "49872"),
#         ("7pqrstsixteen", "7pqrst6teen"),
#         ("zoneight234", "z1234")

#     ])
# def test_convert_line_to_int(input, expected):
#     """Test that spelling is converted to ints."""
#     assert solution.convert_line_to_int(input) == expected

def test_get_ints_from_line(example_2):
    """Test that ints are extracted properly."""
    data = [solution.convert_line_to_int(line) for line in example_2]
    assert solution.get_ints_from_line(data[0]) == [2, 1, 9]

@pytest.mark.parametrize("index,expected", [(0, 29), (1, 83), (2, 13), (3, 24), (4, 42), (5, 14), (6, 76)])
def test_calibration_value_from_ints_example_2(example_2, index, expected):
    """Test that calibration value is extracted properly."""
    lines = [solution.convert_line_to_int(line) for line in example_2]
    values = [solution.get_ints_from_line(line) for line in lines]
    assert solution.get_calibration_value_from_ints(values[index]) == expected

def test_part_2(example_2):
    """Test that part 2 is solved."""
    assert solution.part_2(example_2) == 281