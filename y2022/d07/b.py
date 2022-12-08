import subprocess
import sys
import logging
import math
import os
import re
from functools import reduce
from pprint import pprint

from aoc.input import read_input

LOG = logging.getLogger(__name__)


class Node:
    def __init__(self, name, parent=None, children=None, info=None):
        self.name = name
        self.parent = parent
        self.children = children or {}
        self.info = info or {}

    def __str__(self):
        s = f"<Node '{self.name}' "
        if len(self.children) > 0:
            s += f"children={len(self.children)}"
        return s + f" {self.info}>"

    def add_child(self, node):
        self.children[node.name] = node

    def has_children(self):
        return len(self.children) > 0

    def reduce(self, fn, value=0):
        value = fn(self, value)
        for child in self.children.values():
            value = child.reduce(fn, value)
        return value

    def print(self, indent=""):
        print(f"{indent}{self}")
        for child in self.children.values():
            child.print(indent + "| ")


def create_filesystem(input):
    root = Node("/")
    cur_dir = root
    for section in input.split("\n$ ")[1:]:
        lines = section.split("\n")
        cmd = lines[0]
        response = lines[1:]

        # print("")
        # print(f"command = {cmd} and response = {response}")
        if cmd == "ls":
            for child in response:
                child_size, child_name = child.split(" ")
                node = Node(child_name, parent=cur_dir)
                if child_size != "dir":
                    node.info["size"] = int(child_size)
                cur_dir.add_child(node)

        if cmd[:2] == "cd":
            target = cmd.split(" ")[1]
            if target == "..":
                cur_dir = cur_dir.parent
            else:
                cur_dir = cur_dir.children[target]

    return root


def calc_size(node):
    if node is None:
        return 0

    if "size" in node.info:
        return node.info["size"]

    dir_size = 0
    for child in node.children.values():
        dir_size += calc_size(child)

    # print(f"dir size for {node.name} is {dir_size}")
    node.info["size"] = dir_size
    return dir_size


def solve(input: str):
    available_space = 70000000
    min_space = 30000000

    filesystem = create_filesystem(input)
    # filesystem.print()
    # print("")

    fs_size = calc_size(filesystem)
    # print("")

    remaining_space = available_space - fs_size
    target_dir_size = min_space - remaining_space
    print(f"Available:  {available_space:>10}")
    print(f"Used:       {fs_size:>10}")
    print(f"Remaining:  {remaining_space:>10}")
    print(f"Target dir: {target_dir_size:>10}")

    def get_target_dir(node, value):
        if not node.has_children():
            return value
        ns = node.info["size"]
        if ns >= target_dir_size and ns < value:
            return ns
        return value

    answer = filesystem.reduce(get_target_dir, available_space)
    return answer


if __name__ == "__main__":
    input = read_input(__file__)
    answer = solve(input)
    print("*****")
    print(answer)
    subprocess.run("pbcopy", text=True, input=str(answer))
