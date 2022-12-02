#!/usr/bin/env python3

# Advent of Code 2022
# Day 1

from collections import Counter
import os

file_path = file_path =input_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input_day_01.txt") 


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


def main() -> int:
    lines = read_file(file_path)
    result = get_count(lines)
    c = Counter(result)
    elf = c.most_common(1)[0][0]
    calories = c.most_common(1)[0][1]
    print(f"The elf with the most calories is number {elf}, carrying {calories}")
    top_3 = c.most_common(3)
    print (f"The top 3 elves' calories sum up: {sum([x[1] for x in top_3])}")
    return 0

if __name__ == "__main__":
    exit(main())
