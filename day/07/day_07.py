#!/usr/bin/env python3

# Advent of Code 2022
# Day 7 - No Space Left On Device

import os
import json


file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "day_07_input.txt")


def read_file(input_file: str) -> str:
    with open(input_file) as f:
        buffer = f.readlines()
    return buffer


def parse_cd_command(line: str) -> str:
    elements = line.split()
    return elements[2]


def parse_ls_command(line: str) -> str:
    ...


def parse_dir_command(line: str) -> str:
    elements = line.split()
    return elements[1]


def parse_file_command(line: str) -> tuple:
    elements = line.split()
    return int(elements[0]), elements[1]


def part_1(lines: list) -> int:
    file_system = {}
    current_dir = file_system
    parent_dir = None
    for line in lines:
        if line.startswith('$ cd'):
            # Command to change directory
            tmpdir = parse_cd_command(line)
            if tmpdir == '..':
                current_dir = parent_dir
                if current_dir:
                    parent_dir = current_dir.get('parent')
                else:
                    parent_dir = None
            else:
                # wrkdir = current_dir
                current_dir['children'][tmpdir] = {'type': 'dir', 'parent': current_dir, 'children': []}
                current_dir = current_dir[tmpdir]
        elif line.startswith('$ ls'):
            # Command to list directory contents
            pass
        elif line.startswith('dir'):
            # Directory
            dir_name = parse_dir_command(line)
            current_dir['children'].append({'type': 'dir', 'name': dir_name, 'children': []})
        else:
            # File
            file_size, file_name = parse_file_command(line)
            current_dir['children'].append({'type': 'file', 'name': file_name, 'size': file_size})
    print(json.dumps(file_system, indent=2))

def main() -> int:
    lines = read_file(file_path)
    # Part One
    print(f"Part One: {part_1(lines)}")
    # Part Two
    # print(f"Part Two: {part_2(lines)}")
    return 0


if __name__ == "__main__":
    exit(main())
