#!/usr/bin/env python3

# Advent of Code 2022
# Day 8: Test Treetop Tree House

import os
import pytest
import day_08 as d8

file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "test_day_08_input.txt")


def test_part1():
    """
    - The top-left 5 is visible from the left and top. (It isn't visible from 
        the right or bottom since other trees of height 5 are in the way.)
    - The top-middle 5 is visible from the top and right.
    - The top-right 1 is not visible from any direction; for it to be visible, 
        there would need to only be trees of height 0 between it and an edge.
    - The left-middle 5 is visible, but only from the right.
    - The center 3 is not visible from any direction; for it to be visible, 
        there would need to be only trees of at most height 2 between it and an 
        edge.
    - The right-middle 3 is visible from the right.
    - In the bottom row, the middle 5 is visible, but the 3 and 4 are not.
    """

    lines = d8.read_file(file_path)
    lines = [line.strip() for line in lines]
    result = d8.part_1(lines)
    assert result == 21


def test_part2():
    """

    """
    lines = d8.read_file(file_path)
    result = d8.part_2(lines)
    # assert result == 24933642


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
