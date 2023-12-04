"""
Advent of Code: Day 01, 2023
Name: Trebuchet?!
"""

# Standard library imports
from pathlib import Path
import sys

# Utility functions
def get_ints_from_line(line):
    ints = []
    for char in line:
        try:
            ints.append(int(char))
        except:
            pass
    return ints

def get_calibration_value_from_ints(ints):
    value = ints[0] * 10 + ints[-1]
    return value

def get_int_words():
    spelling = "one, two, three, four, five, six, seven, eight, nine"
    spelling = spelling.split(", ")
    words = {word: number for number, word in enumerate(spelling, start = 1)}
    return words

def convert_line_to_int(text, start_index = 0):
    int_words = get_int_words()
    index = start_index
    while index < len(text):
        for word in int_words:
            if text[index:].startswith(word):
                # text = text[:index] + str(int_words[word]) + text[index + len(word):]
                text = text[:index] + str(int_words[word]) + text[index + 1:]
        return convert_line_to_int(text, start_index = index + 1)
    return text

# Solutions
def parse_data(puzzle_input):
    """Parse input."""
    puzzle_input = puzzle_input.splitlines()
    return puzzle_input

def part_1(data):
    """What is the sum of all of the calibration values?"""
    values = []
    for line in data:
        ints = get_ints_from_line(line)
        value = get_calibration_value_from_ints(ints)
        values.append(value)
    result = sum(values)
    return result

def part_2(data):
    """Solve part 2."""
    data = [convert_line_to_int(line) for line in data]
    return part_1(data)

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