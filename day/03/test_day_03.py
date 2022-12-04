#!/usr/bin/env python3

# Advent of Code 2022
# Day 2 - Test Rock Paper Scissors

import os
import pytest
import day_03 as d3

file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "test_day_03_input.txt")


def test_part1():
    # In the above example, the priority of the item type that appears 
    # in both compartments of each rucksack is 
    # 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); 
    # the sum of these is 157.
    lines = d3.read_file(file_path)
    assert d3.part_1(lines) == 157
    
def test_part2():
    # Priorities for these items must still be found to organize 
    # the sticker attachment efforts: here, they are 18 (r) 
    # for the first group and 52 (Z) for the second group. 
    # The sum of these is 70.
    lines = d3.read_file(file_path)
    assert d3.part_2(lines) == 70


if __name__ == "__main__":
    pytest.main()
