#!/usr/bin/env python3

# Advent of Code 2022
# Day 1 - Calorie Counting

from collections import Counter
import os

file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "day_01_input.txt")


def read_file(input_file: str) -> str:
    with open(input_file) as f:
        lines = f.readlines()
    return lines


def get_count(lines: str) -> dict:
    result_dict = {}

    elf = 1
    for line in lines:
        stripped_line = line.strip()
        if stripped_line:
            result_dict[elf] = result_dict.get(elf, 0) + int(stripped_line)
        else:
            elf += 1

    return result_dict


def part_1(data: dict) -> list:
    c = Counter(data)
    return c.most_common(1)[0][0], c.most_common(1)[0][1]


def part_2(data: dict) -> int:
    c = Counter(data)
    top_3 = c.most_common(3)
    return sum([x[1] for x in top_3])


def main() -> int:
    lines = read_file(file_path)
    data = get_count(lines)

    # Part One
    print("Part One: The elf %s carries the most calories: %d" % part_1(data))

    # Part Two
    print(f"Part Two: The total calories in the top 3 elves is {part_2(data)}")
    return 0


if __name__ == "__main__":
    exit(main())
