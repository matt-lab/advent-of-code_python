"""
Advent of Code: Day {DAY}, {YEAR}
Name: {PUZZLE_NAME}
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