#!/usr/bin/env python3

# Advent of Code 2022
# Day 4 - Test Camp Cleanup

import os
import pytest
import day_04 as d4

file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "test_day_04_input.txt")


def test_part1():
    """Some of the pairs have noticed that one of their assignments fully 
    contains the other. For example, 2-8 fully contains 3-7, and 6-6 is 
    fully contained by 4-6. In pairs where one assignment fully contains 
    the other, one Elf in the pair would be exclusively cleaning sections 
    their partner will already be cleaning, so these seem like the most in 
    need of reconsideration. In this example, there are 2 such pairs.
    """
    
    lines = d4.read_file(file_path)
    assert d4.part_1(lines) == 2


def test_part2():
    """In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't 
    overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 
    2-6,4-8) do overlap: So, in this example, the number of overlapping 
    assignment pairs is 4.
    """

    lines = d4.read_file(file_path)
    assert d4.part_2(lines) == 4


if __name__ == "__main__":
    pytest.main()
