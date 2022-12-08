#!/usr/bin/env python3

# Advent of Code 2022
# Day 6 - Tuning Trouble

import os

file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "day_06_input.txt")


def read_file(input_file: str) -> str:
    with open(input_file) as f:
        buffer = f.read()
    return buffer


def part_1(buffer: str) -> int:
    SOP_LEN = 4
    for i in range(len(buffer) - SOP_LEN):
        if len(set(buffer[i:i+SOP_LEN])) == SOP_LEN:
            return i + SOP_LEN
    return None


def part_2(buffer: str) -> int:
    SOM_LEN = 14
    for i in range(len(buffer) - SOM_LEN):
        if len(set(buffer[i:i+SOM_LEN])) == SOM_LEN:
            return i + SOM_LEN
    return None


def main() -> int:
    buffer = read_file(file_path)
    # Part One
    print(f"Part One: {part_1(buffer)}")
    # Part Two
    print(f"Part Two: {part_2(buffer)}")
    return 0


if __name__ == "__main__":
    exit(main())
