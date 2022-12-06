import pytest

from .b import solve

@pytest.mark.parametrize("input,expected", [

])
def test_solve(input, expected):
    answer = solve(input)
    assert answer == expected
