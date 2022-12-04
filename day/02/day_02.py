#!/usr/bin/env python3

# Advent of Code 2022
# Day 2

import os

file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "day_02_input.txt")


def read_file(input_file: str) -> str:
    with open(input_file) as f:
        lines = f.readlines()
    return lines


def resolve_winner(abc: str, xyz: str) -> str:
    """Return the winner of the round.
    A for Rock, B for Paper, and C for Scissors
    X for Rock, Y for Paper, and Z for Scissors
    """
    rps = {
        "A": {
            "X": "",
            "Y": "Y",
            "Z": "A"
        },
        "B": {
            "X": "B",
            "Y": "",
            "Z": "Z"
        },
        "C": {
            "X": "X",
            "Y": "C",
            "Z": ""
        }
    }
    return rps[abc][xyz]


def resolve_endgame(abc: str, xyz: str) -> str:
    """Return the winner of the round.
    A for Rock, B for Paper, and C for Scissors
    X for Lose, Y for Tie, and Z for Win
    """
    rps = {
        "A": {
            "X": "Z",
            "Y": "X",
            "Z": "Y"
        },
        "B": {
            "X": "X",
            "Y": "Y",
            "Z": "Z"
        },
        "C": {
            "X": "Y",
            "Y": "Z",
            "Z": "X"
        }
    }
    return rps[abc][xyz]


def get_points(ABC: str, XYZ: str) -> int:
    """Return the number of points this solution earned
        (1 for Rock, 2 for Paper, and 3 for Scissors) 
    plus the score for the outcome of the round 
        (0 if you lost, 3 if the round was a draw, and 6 if you won).
    """
    points_for_XYZ = ord(XYZ) - 87
    winner = resolve_winner(ABC, XYZ)
    points_for_winner = 6 if winner == XYZ else 3 if winner == "" else 0
    return points_for_XYZ + points_for_winner


def part_1(lines: list) -> int:
    points = []
    for line in lines:
        ABC, XYZ = line.split()
        points.append(get_points(ABC, XYZ))
    return points


def part_2(lines: list) -> int:
    points = []
    for line in lines:
        ABC, goal = line.split()
        XYZ = resolve_endgame(ABC, goal)
        points.append(get_points(ABC, XYZ))
    return points


def main() -> int:
    lines = read_file(file_path)
    # Part 1
    print(f"First strategy: {sum(part_1(lines))}")
    # Part 2
    print(f"Endgame: {sum(part_2(lines))}")
    return 0


if __name__ == "__main__":
    exit(main())
