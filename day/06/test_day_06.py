#!/usr/bin/env python3

# Advent of Code 2022
# Day 6 - Test Tuning Trouble

import pytest
import day_06 as d6


def test_part1():
    """
    start-of-packet is a sequence of 4 different characters.

    mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 7
    bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5
    nppdvjthqldpwncqszvftbrmjlhg: first marker after character 6
    nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 10
    zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 11
    """

    assert d6.part_1("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert d6.part_1("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert d6.part_1("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert d6.part_1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert d6.part_1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11


def test_part2():
    """
    start-of-message is a sequence of 14 different characters.

    mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
    bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
    nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
    nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
    zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26
    """

    assert d6.part_2("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
    assert d6.part_2("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    assert d6.part_2("nppdvjthqldpwncqszvftbrmjlhg") == 23
    assert d6.part_2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    assert d6.part_2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26


if __name__ == "__main__":
    pytest.main()
