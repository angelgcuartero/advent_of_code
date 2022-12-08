#!/usr/bin/env python3

# Advent of Code 2022
# Day 1 - Test Calorie Counting

from collections import Counter
import os
import pytest
import day_01 as d1

file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "test_day_01_input.txt")


# Part 1
def test_count():
    lines = d1.read_file(file_path)
    assert len(lines) == 14


def test_part_1_get_calories_count():
    lines = d1.read_file(file_path)
    data = d1.get_count(lines)
    assert len(data) == 5
    elf, count = d1.part_1(data)
    assert elf == 4
    assert count == 24000

# Part 2
def test_part_2_top_3_sum_calories():
    lines = d1.read_file(file_path)
    data = d1.get_count(lines)
    top_3 = d1.part_2(data)
    assert top_3 == 45000


if __name__ == "__main__":
    pytest.main()
