import pytest

from .a import solve


@pytest.mark.parametrize(
    "input,expected",
    [
        (
            """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""",
            24,
        )
    ],
)
def test_solve(input, expected):
    answer = solve(input)
    assert answer == expected
