#!/usr/bin/env python3

# Advent of Code 2022
# Day 7 - Test No Space Left On Device

import os
import pytest
import day_07 as d7

file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "test_day_07_input.txt")


def test_part1():
    """
    To begin, find all of the directories with a total size of at
    most 100000, then calculate the sum of their total sizes. In the
    example above, these directories are a and e; the sum of their
    total sizes is 95437 (94853 + 584). (As in this example, this
    process can count files more than once!)
    """

    lines = d7.read_file(file_path)
    result = d7.part_1(lines)
    assert 'a' in result
    assert 'e' in result
    assert result['a'] == 94853
    assert result['e'] == 584


# def test_part2():
#     """
#     """

#     assert True


if __name__ == "__main__":
    pytest.main()
