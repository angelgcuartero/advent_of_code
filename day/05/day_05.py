#!/usr/bin/env python3

# Advent of Code 2022
# Day 5 - Supply Stacks

from collections import deque
import os
import textwrap

file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "day_05_input.txt")


def read_file(input_file: str) -> str:
    with open(input_file) as f:
        lines = f.readlines()
    return lines


def split_data_file(lines) -> tuple:
    for i, line in enumerate(lines):
        if line.lstrip().startswith("["):
            continue
        else:
            return int(line.strip()[-1]), lines[:i], lines[i + 2:]


def parse_stacks(lines, num_stacks) -> list:
    NUM_CHARS = 4
    stacks = [deque() for _ in range(num_stacks)]
    for line in lines:
        splitted_line = textwrap.wrap(line, NUM_CHARS, drop_whitespace=False)
        for i, crate in enumerate(splitted_line):
            crate_char = crate.strip("[] ")
            if crate_char:
                stacks[i].appendleft(crate_char)

    return stacks


def parse_instructions_cratemover_9000(instructions, stacks):
    NUM_ELEMS = 1
    FROM = 3
    TO = 5
    for instruction in instructions:
        line = instruction.split()
        for _ in range(int(line[NUM_ELEMS])):
            elem = stacks[int(line[FROM])-1].pop()
            stacks[int(line[TO])-1].append(elem)
    return "".join([stacks[i].pop() for i in range(len(stacks))])


def parse_instructions_cratemover_9001(instructions, stacks):
    NUM_ELEMS = 1
    FROM = 3
    TO = 5
    for instruction in instructions:
        line = instruction.split()
        tmp_stack = deque()
        for _ in range(int(line[NUM_ELEMS])):
            elem = stacks[int(line[FROM])-1].pop()
            tmp_stack.appendleft(elem)
        stacks[int(line[TO])-1].extend(tmp_stack)
    return "".join([stacks[i].pop() for i in range(len(stacks))])


def part_1(lines: list) -> int:
    num_stacks, crate_data, instructions = split_data_file(lines)
    stacks = parse_stacks(crate_data, num_stacks)
    result = parse_instructions_cratemover_9000(instructions, stacks)
    return result


def part_2(lines: list) -> int:
    num_stacks, crate_data, instructions = split_data_file(lines)
    stacks = parse_stacks(crate_data, num_stacks)
    result = parse_instructions_cratemover_9001(instructions, stacks)
    return result


def main() -> int:
    lines = read_file(file_path)
    # Part 1
    print(f"Part 1: {part_1(lines)}")
    # Part 2
    print(f"Part 2: {part_2(lines)}")
    return 0


if __name__ == "__main__":
    exit(main())
