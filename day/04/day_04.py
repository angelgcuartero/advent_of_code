#!/usr/bin/env python3

# Advent of Code 2022
# Day 4 - Camp Cleanup

import os

file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "day_04_input.txt")


def read_file(input_file: str) -> str:
    with open(input_file) as f:
        lines = f.readlines()
    return lines


def get_sets(line: str) -> tuple:
    p1, p2 = line.strip().split(",")
    pl11, pl12 = p1.split("-")
    pl21, pl22 = p2.split("-")
    s1 = set(range(int(pl11), int(pl12) + 1))
    s2 = set(range(int(pl21), int(pl22) + 1))
    return s1, s2


def part_1(lines: list) -> int:
    num_pairs = 0
    for line in lines:
        s1, s2 = get_sets(line)
        if s1.issubset(s2) or s2.issubset(s1):
            num_pairs += 1
    return num_pairs


def part_2(lines: list) -> int:
    num_pairs = 0
    for line in lines:
        s1, s2 = get_sets(line)
        if not s1.isdisjoint(s2):
            num_pairs += 1
    return num_pairs


def main() -> int:
    lines = read_file(file_path)
    # Part 1
    print(f"Part 1: {part_1(lines)}")
    # Part 2
    print(f"Part 2: {part_2(lines)}")
    return 0


if __name__ == "__main__":
    exit(main())
