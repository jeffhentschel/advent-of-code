import pytest

from .a import solve


@pytest.mark.parametrize(
    "input,expected",
    [
        (
            """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""",
            13,
        )
    ],
)
def test_solve(input, expected):
    answer = solve(input)
    assert answer == expected
