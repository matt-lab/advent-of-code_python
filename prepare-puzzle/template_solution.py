"""
Advent of Code: Day {DAY}, {YEAR}
Name: {PUZZLE_NAME}
"""

# Standard library imports
from pathlib import Path
import sys

def parse_data(puzzle_input):
    """Parse input."""

def part_1(data):
    """Solve part 1."""

def part_2(data):
    """Solve part 2."""

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