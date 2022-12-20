import pytest

from .a import Atlas, solve


@pytest.mark.parametrize(
    "here,there,expected",
    [
        ((1, 2), (1, 3), False),
        ((0, 0), (1, 0), True),
        ((4, 1), (4, 2), False),
        ((4, 1), (3, 1), True),
        ((3, 5), (2, 5), False),
        ((2, 4), (2, 5), True),
    ],
)
def test_valid_step(here, there, expected):
    input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".splitlines()
    map = Atlas(input)
    assert map.valid_step(here, there) == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        (
            """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""",
            31,
        )
    ],
)
def test_solve(input, expected):
    answer = solve(input)
    assert answer == expected
