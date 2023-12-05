"""
Downloads the input for one Advent of Code puzzle, if possible.
Uses https://pypi.org/project/advent-of-code-data/ if it's available.
Otherwise, does nothing.
Adapt from Github user @gahjelle script.
"""

from pathlib import Path
import sys
from aocd.models import Puzzle


def download(year, day):
    """Get input and write it to input.txt inside the puzzle folder"""
    puzzle = Puzzle(year=year, day=day)

    # Prepare directories
    year_path = Path(__file__).parent.parent / str(year)
    year_path.mkdir(exist_ok = True)
    day_path = Path(year_path) / f"{day:02d}"
    day_path.mkdir(exist_ok = True)

    # Download input data
    output_path = Path(day_path) / "input.txt"
    output_path.write_text(puzzle.input_data)

    # Download example data
    for index, example in enumerate(puzzle.examples, start = 1):
        output_path = output_path.with_stem(f"example_{index}")
        output_path.write_text(example.input_data)

    # Write template solution
    template_path = Path(__file__).parent / "template_solution.py"
    solution_path = Path(day_path) / "solution.py"
    if not solution_path.exists():
        template = template_path.read_text()
        template = template.replace("{YEAR}", str(year))
        template = template.replace("{DAY}", f"{day:02d}")
        template = template.replace("{PUZZLE_NAME}", puzzle.title)
        solution_path.write_text(template)

    # Write template test
    template_path = Path(__file__).parent / "template_test.py"
    test_path = Path(day_path) / "solution_test.py"
    if not test_path.exists():
        template = template_path.read_text()
        template = template.replace("{YEAR}", str(year))
        template = template.replace("{DAY}", f"{day:02d}")
        template = template.replace("{PUZZLE_NAME}", puzzle.title)
        test_path.write_text(template)

    # Add README with link to puzzle text
    readme_path = output_path.with_name("README.md")
    readme_path.write_text(
        f"# {puzzle.title}\n\n"
        f"**Advent of Code: Day {day}, {year}**\n\n"
        f"See {puzzle.url}\n"
    )

if __name__ == "__main__":
    try:
        # Read year and day from command line
        download(year=int(sys.argv[1]), day=int(sys.argv[2]))
    except Exception as err:
        # Catch exceptions so that Copier doesn't clean up directories
        print(f"Download of input failed: {err}")
        raise SystemExit()