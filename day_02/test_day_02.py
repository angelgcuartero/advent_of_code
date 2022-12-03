#!/usr/bin/env python3

# Advent of Code 2022
# Day 2 - Test Rock Paper Scissors

import os
import pytest
import day_02 as d2

file_path = input_file = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "test_day_02_input.txt")


def test_count_lines():
    lines = d2.read_file(file_path)
    assert len(lines) == 3


def test_rps_file_valid_content():
    lines = d2.read_file(file_path)
    for line in lines:
        ABC, XYZ = line.split()
        assert ABC in "ABC"
        assert XYZ in "XYZ"


def test_rps_file_content():
    lines = d2.read_file(file_path)
    points = []
    for line in lines:
        ABC, XYZ = line.split()
        points.append(d2.get_points(ABC, XYZ))
    assert points == [8, 1, 6]


def test_rps_file_content_endgame():
    lines = d2.read_file(file_path)
    points = []
    for line in lines:
        ABC, XYZ = line.split()
        ZYX = d2.resolve_endgame(ABC, XYZ)
        points.append(d2.get_points(ABC, ZYX))
    assert points == [4, 1, 7]


if __name__ == "__main__":
    # os.chdir(os.path.dirname(os.path.abspath(__file__)))
    pytest.main()
