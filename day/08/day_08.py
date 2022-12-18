#!/usr/bin/env python3

# Advent of Code 2022
# Day 7 - No Space Left On Device

import copy
import os

terrain = []
terrain_transposed = []
terrain_visible = []
terrain_width = 0
terrain_height = 0

file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "day_08_input.txt")


def read_file(input_file: str) -> str:
    with open(input_file) as f:
        buffer = f.readlines()
    return buffer


def generate_map(lines: list) -> list:
    """
    Generate a map of the area
    """
    map = []
    for line in lines:
        map.append([int(x) for x in line])
    return map


def generate_transposed():
    return list(map(list, zip(*terrain)))


def check_column(x: int, y: int) -> bool:
    """
    Check if a given position is visible for a column
    """
    global terrain
    global terrain_transposed
    global terrain_height

    tree_height = terrain[y][x]
    col = terrain_transposed[x]
    for i in range(y):
        if col[i] >= tree_height:
            up = False
            break
    else:
        up = True

    for i in range(y + 1, terrain_height):
        if col[i] >= tree_height:
            down = False
            break
    else:
        down = True
    return up or down


def check_row(x: int, y: int) -> bool:
    """
    Check if a given position is visible for a row
    """
    global terrain
    global terrain_width

    tree_height = terrain[y][x]
    row = terrain[y]
    for i in range(x):
        if row[i] >= tree_height:
            left = False
            break
    else:
        left = True

    for i in range(x + 1, terrain_width):
        if row[i] >= tree_height:
            right = False
            break
    else:
        right = True
    return left or right


def generate_visible():
    """
    Check if a given position is visible from the top-left corner
    """
    global terrain
    global terrain_transposed
    global terrain_width
    global terrain_height

    terrain_visible = copy.deepcopy(terrain)

    for y in range(terrain_width):
        for x in range(terrain_height):
            if x == 0 or y == 0:
                result = True
            elif x == terrain_width - 1 or y == terrain_height - 1:
                result = True
            else:
                result = check_column(x, y) or check_row(x, y)
            terrain_visible[y][x] = result
    return terrain_visible


def is_visible(x: int, y: int) -> bool:
    return terrain_visible[y][x]


def part_1(lines: list) -> int:
    """
    """
    global terrain
    global terrain_transposed
    global terrain_visible
    global terrain_width
    global terrain_height

    terrain = generate_map(lines)
    terrain_width = len(terrain)
    terrain_height = len(terrain[0])
    terrain_transposed = generate_transposed()
    terrain_visible = generate_visible()

    count = 0
    for y in range(terrain_width):
        count += sum(terrain_visible[y])

    return count


def part_2(lines: list) -> int:
    """
    """
    return 0


def main() -> int:
    global terrain
    global terrain_transposed

    lines = read_file(file_path)
    lines = [line.strip() for line in lines]
    # Part One
    print(f"Part One: {part_1(lines)}")
    # Part Two
    print(f"Part Two: {part_2(lines)}")
    return 0


if __name__ == "__main__":
    exit(main())
