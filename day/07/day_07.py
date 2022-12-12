#!/usr/bin/env python3

# Advent of Code 2022
# Day 7 - No Space Left On Device

from enum import Enum
import os


file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "day_07_input.txt")


class NT(str, Enum):
    DIR = 'dir'
    FILE = 'file'


# @dataclass
class Node:
    def __init__(self,
                 name: str,
                 type: str,
                 parent: int,
                 size: int = None):
        self.id = id(self)
        self.name = name
        self.type = type
        self.size = size
        self.parent = parent
        self.children = []

    def __repr__(self):
        return f"{self.name} ({self.type})"

    def __str__(self):
        return f"{self.name} ({self.type})"

    def get_size(self):
        if self.type == NT.DIR and self.size is None:
            self.size = sum([child.get_size() for child in self.children])
        return self.size


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


def get_node_by_name(file_system: dict, name: str) -> Node:
    for node in file_system.values():
        if node.name == name and node.type == NT.DIR:
            return node
    return None


def parse_file_system(lines) -> dict:
    file_system = {}
    current_dir_id = None

    for line in lines:
        line = line.strip()
        if line.startswith('$ cd'):
            # Command to change directory
            parsed_dir = parse_cd_command(line)
            if parsed_dir == '..':
                current_dir_id = file_system[current_dir_id].parent if \
                    current_dir_id in file_system else None
            else:
                # Case for root directory
                if line == '$ cd /':
                    node = Node('/', NT.DIR, None)
                    file_system[node.id] = node
                    current_dir_id = node.id
                    continue
                name_to_search = '/'.join([
                    file_system[current_dir_id].name if
                    current_dir_id is not None else '',
                    parsed_dir]
                )
                node_to_search = get_node_by_name(file_system, name_to_search)
                current_dir_id = node_to_search.id
        elif line.startswith('$ ls'):
            # Command to list directory contents
            parse_ls_command(line)
        elif line.startswith('dir'):
            # Directory
            parsed_dir = parse_dir_command(line)
            name_to_set = '/'.join(
                [
                    file_system[current_dir_id].name,
                    parsed_dir
                ]
            )
            node = Node(name_to_set, NT.DIR, current_dir_id)
            file_system[node.id] = node
            file_system[current_dir_id].children.append(node)
        else:
            # File
            file_size, file_name = parse_file_command(line)

            name_to_set = '/'.join(
                [
                    file_system[current_dir_id].name,
                    file_name
                ]
            )
            node = Node(name_to_set, NT.FILE, current_dir_id, file_size)
            file_system[node.id] = node
            file_system[current_dir_id].children.append(node)

    return file_system


def get_minimal_dir(file_system: dict) -> Node:
    TOTAL_DISK_SPACE = 70_000_000
    REQUIRED_FREE_SPACE = 30_000_000

    root_size = get_node_by_name(file_system, '/').get_size()

    REQUIRED_TO_DELETE = TOTAL_DISK_SPACE - root_size - REQUIRED_FREE_SPACE

    minimal_dir = None
    for node in file_system.values():
        if node.type == NT.DIR and node.get_size() > abs(REQUIRED_TO_DELETE):
            if minimal_dir is None or node.get_size() < minimal_dir.get_size():
                minimal_dir = node
    return minimal_dir


def part_1(lines: list) -> int:
    TOP_SIZE = 100000

    file_system = parse_file_system(lines)
    result = sum([x.get_size() if
                  x.type == NT.DIR and x.get_size() < TOP_SIZE else 0
                  for x in file_system.values()])
    return result


def part_2(lines: list) -> int:
    file_system = parse_file_system(lines)

    node = get_minimal_dir(file_system)
    print(node.name, node.get_size())
    return node.get_size()


def main() -> int:
    lines = read_file(file_path)
    # Part One
    print(f"Part One: {part_1(lines)}")
    # Part Two
    print(f"Part Two: {part_2(lines)}")
    return 0


if __name__ == "__main__":
    exit(main())
