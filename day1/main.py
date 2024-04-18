#! python
import argparse
import re
import sys


def parse_file(file_location: str):

    with open(file_location, "r+", encoding="utf-8") as f:
        lines = [line.strip("\n") for line in f.readlines()]

    return lines


def compute_calibration(obfuscated_list) -> int:

    pattern = r"\d"
    number_lines = ["".join(re.findall(pattern, line)) for line in obfuscated_list]
    not_empty = filter(lambda line: len(line) > 0, number_lines)
    coordinates = list(map(lambda line: int(f"{line[0]}{line[-1]}"), not_empty))

    return sum(coordinates)


def main(file_location: str):
    raw_lines = parse_file(file_location)
    coordinates = compute_calibration(raw_lines)

    sys.stdout.write(f"Unobfuscated Coordinates are: {coordinates}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="AoC Day 1.")
    parser.add_argument(
        "file_location", type=str, help="The location of the file to process"
    )

    args = parser.parse_args()

    main(args.file_location)
