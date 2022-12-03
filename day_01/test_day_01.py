#!/usr/bin/env python3

# Advent of Code 2022
# Day 1 - Test Inventory

from collections import Counter
import os
import pytest
import day_01 as d1

file_path = input_file = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "test_day_01_input.txt")

# Part 1


def test_count():
    lines = d1.read_file(file_path)
    assert len(lines) == 14


def test_get_calories_count():
    lines = d1.read_file(file_path)
    result = d1.get_count(lines)
    assert len(result) == 5
    c = Counter(result)
    print(c.most_common(1))


def test_top_3():
    lines = d1.read_file(file_path)
    result = d1.get_count(lines)
    c = Counter(result)
    top_3 = c.most_common(3)
    assert top_3 == [(4, 24000), (3, 11000), (5, 10000)]
    print(sum([x[1] for x in top_3]))


if __name__ == "__main__":
    # os.chdir(os.path.dirname(os.path.abspath(__file__)))
    pytest.main()
