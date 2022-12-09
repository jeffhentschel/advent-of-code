import pytest

from .a import solve


@pytest.mark.parametrize(
    "input,expected",
    [
        (
            """30373
25512
65332
33549
35390""",
            21,
        )
    ],
)
def test_solve(input, expected):
    answer = solve(input)
    assert answer == expected
