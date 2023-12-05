"""
Advent of Code: Day 02, 2023
Name: Cube Conundrum
"""

# Standard library imports
from pathlib import Path
import re

def parse_data(puzzle_input):
    """Parse input."""
    lines = puzzle_input.splitlines()
    games = []
    for line in lines:
        subsets = []
        id = int(re.findall(r'^Game (\d+):', line)[0])
        subsets_str = re.split(";", re.split(":", line)[1])
        for subset_str in subsets_str:
            cubes = []
            cubes_str = re.findall(r"(\d+) (red|green|blue)", subset_str)
            for cube_str in cubes_str:
                cubes.append({cube_str[1]: int(cube_str[0])})
            subsets.append(cubes)
        games.append({"id": id, "subsets": subsets})
    return games

def is_valid_game(subsets, max_cubes = {"red": 12, "green": 13, "blue": 14}):
    """Check if game is valid."""
    could_be_valid = True
    for subset in subsets:
        for cube in subset:
            for colour in cube:
                if cube[colour] > max_cubes[colour]:
                    could_be_valid = False
                    break
    return could_be_valid

def get_valid_ids(games, max_cubes = {"red": 12, "green": 13, "blue": 14}):
    """Get valid ids."""
    ids = []
    for game in games:
        if is_valid_game(game["subsets"], max_cubes):
            ids.append(game["id"])
    return ids

def get_min_cubes(subsets):
    """Get minimum number of cubes."""
    min_cubes = {"red": 0, "green": 0, "blue": 0}
    for subset in subsets:
        for cube in subset:
            for colour in cube:
                if cube[colour] > min_cubes[colour]:
                    min_cubes[colour] = cube[colour]
    return min_cubes

def part_1(data, max_cubes = {"red": 12, "green": 13, "blue": 14}):
    """Solve part 1."""
    ids = get_valid_ids(data, max_cubes)
    result = sum(ids)
    return result
        
def part_2(data):
    """Solve part 2."""
    scores = []
    for game in data:
        min_cubes = get_min_cubes(game["subsets"])
        score = 1
        for colour in min_cubes:
            score *= min_cubes[colour]
        scores.append(score)
    result = sum(scores)
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