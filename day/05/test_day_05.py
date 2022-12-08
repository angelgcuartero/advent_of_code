#!/usr/bin/env python3

# Advent of Code 2022
# Day 5 - Supply Stacks

import os
import pytest
import day_05 as d5

file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "test_day_05_input.txt")


def test_part1():
    """
        [D]
    [N] [C]
    [Z] [M] [P]
     1   2   3

    move 1 from 2 to 1
    move 3 from 1 to 3
    move 2 from 2 to 1
    move 1 from 1 to 2

    Results in:

            [Z]
            [N]
            [D]
    [C] [M] [P]
     1   2   3

    The Elves just need to know which crate will end up on top of
    each stack; in this example, the top crates are C in stack 1,
    M in stack 2, and Z in stack 3, so you should combine these
    together and give the Elves the message CMZ.
    """

    lines = d5.read_file(file_path)
    assert d5.part_1(lines) == "CMZ"


def test_part2():
    """
        [D]
    [N] [C]
    [Z] [M] [P]
     1   2   3

    move 1 from 2 to 1
    move 3 from 1 to 3
    move 2 from 2 to 1
    move 1 from 1 to 2

    Results in:
            [D]
            [N]
            [Z]
    [M] [C] [P]
    1   2   3
    """

    lines = d5.read_file(file_path)
    assert d5.part_2(lines) == "MCD"


if __name__ == "__main__":
    pytest.main()
