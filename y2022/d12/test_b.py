import pytest

from .b import Atlas, solve

#   0 1 2 3 4 5 6 7
# 0 S a b q p o n m
# 1 a b c r y x x l
# 2 a c c s z E x k
# 3 a c c t u v w j
# 4 a b d e f g h i

example = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


@pytest.mark.parametrize(
    "here,there,expected",
    [
        ((1, 2), (1, 3), True),
        ((1, 1), (1, 0), True),
        ((1, 0), (1, 1), True),
        ((1, 4), (1, 3), False),
        ((3, 5), (2, 5), True),
    ],
)
def test_valid_step(here, there, expected):
    input = example.splitlines()
    map = Atlas(input)
    assert map.valid_step(here, there) == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        (example, 29),
    ],
)
def test_solve(input, expected):
    answer = solve(input)
    assert answer == expected
