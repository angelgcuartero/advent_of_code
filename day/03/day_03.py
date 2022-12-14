#!/usr/bin/env python3

# Advent of Code 2022
# Day 3 - Rucksack Reorganization

import os
import string

file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "day_03_input.txt")


def read_file(input_file: str) -> str:
    with open(input_file) as f:
        lines = f.readlines()
    return lines


def get_priority(c: str) -> int:
    # Lowercase item types a through z have priorities 1 through 26.
    # Uppercase item types A through Z have priorities 27 through 52.

    if c in string.ascii_lowercase:
        return ord(c) - ord('a') + 1
    elif c in string.ascii_uppercase:
        return ord(c) - ord('A') + 27
    else:
        return 0


def get_item(line: str) -> str:
    first_half = line[:len(line) // 2].strip()
    second_half = line[len(line) // 2:].strip()
    return (set(first_half) & set(second_half)).pop()


def part_1(lines: list) -> int:
    priorities = []
    for line in lines:
        c = get_item(line)
        p = get_priority(c)
        priorities.append(p)
    return sum(priorities)


def part_2(lines: list) -> int:
    priorities = []
    local_wrk = []
    counter = 3
    for line in lines:
        if counter == 0:
            counter = 3
            c = set(local_wrk[0]) & set(local_wrk[1]) & set(local_wrk[2])
            priorities.append(get_priority(c.pop()))
            local_wrk = []
        local_wrk.append(line.strip())
        counter -= 1
    else:
        c = set(local_wrk[0]) & set(local_wrk[1]) & set(local_wrk[2])
        priorities.append(get_priority(c.pop()))
    return sum(priorities)


def main() -> int:
    lines = read_file(file_path)
    # Part One
    print(f"Part One: {part_1(lines)}")
    # Part Two
    print(f"Part Two: {part_2(lines)}")
    return 0


if __name__ == "__main__":
    exit(main())
