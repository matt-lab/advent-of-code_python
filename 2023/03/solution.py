"""
Advent of Code: Day 03, 2023
Name: Gear Ratios
"""

# Standard library imports
from pathlib import Path
import re

def parse_data(puzzle_input):
    """Parse input."""
    entities = []
    lines = puzzle_input.splitlines()
    for line_index, line in enumerate(lines, start = 0):
        for match in re.finditer(r"(\d+)|([^\d\.])", line):
            entities.append({
                "is_number": match.group(1) is not None,
                "is_symbol": match.group(2) is not None,
                "text": match.group(0),
                "x_start": match.start(),
                "x_end": match.end() - 1,
                "y": line_index
            })
    return entities

def entities_are_adjacent(entity_1, entity_2):
    """Check if two entities are adjacent."""
    y_distance = abs(entity_1["y"] - entity_2["y"])
    if y_distance > 1:
        return False
    x_distances = []
    for x_1 in range(entity_1["x_start"], entity_1["x_end"] + 1):
        for x_2 in range(entity_2["x_start"], entity_2["x_end"] + 1):
            x_distances.append(abs(x_1 - x_2))
    return min(x_distances) <= 1

def get_adjacent_entities(entity, entities):
    """Get all entities adjacent to the given entity."""
    adjacent_entities = []
    for other_entity in entities:
        if entity == other_entity:
            continue
        if entities_are_adjacent(entity, other_entity):
            adjacent_entities.append(other_entity)
    return adjacent_entities

def get_part_numbers(entities):
    """Part numbers are numbers that are adjacent to a symbol"""
    symbols = [entity for entity in entities if entity["is_symbol"]]
    part_numbers = []
    for entity in entities:
        if entity["is_number"]:
            adjacent_entities = get_adjacent_entities(entity, symbols)
            if len(adjacent_entities) > 0:
                part_numbers.append(entity)
    return part_numbers

def get_gears(entities):
    """Gears are asterisks that are adjacent to exactly two part numbers"""
    asterisks = [entity for entity in entities if entity["text"] == "*"]
    numbers = [entity for entity in entities if entity["is_number"]]
    gears = []
    for entity in asterisks:
        adjacent_entities = get_adjacent_entities(entity, numbers)
        if len(adjacent_entities) == 2:
            gears.append({
                "gear": entity,
                "part_numbers": adjacent_entities
            })
    return gears

def get_gear_ratio(gear):
    """Get the gear ratio for a given gear."""
    gear_ratio = 1
    for part_number in gear["part_numbers"]:
        gear_ratio *= int(part_number["text"])
    return gear_ratio

def part_1(data):
    """Solve part 1."""
    result = 0
    part_numbers = get_part_numbers(data)
    for part_number in part_numbers:
        result += int(part_number["text"])
    return result


def part_2(data):
    """Solve part 2."""
    gears = get_gears(data)
    gear_ratios = [get_gear_ratio(gear) for gear in gears]
    result = sum(gear_ratios)
    return result


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