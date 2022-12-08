import pytest

from .b import solve

t1 = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


@pytest.mark.parametrize("input,expected", [(t1, 24933642)])
def test_solve(input, expected):
    answer = solve(input)
    assert answer == expected
