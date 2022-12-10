import pytest

from .b import follow, solve


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
            1,
        ),
        (
            """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""",
            36,
        ),
    ],
)
def test_solve(input, expected):
    answer = solve(input)
    assert answer == expected


@pytest.mark.parametrize(
    "head,tail,expected_tail",
    [
        ([5, 5], [5, 5], [5, 5]),
        ([6, 5], [5, 5], [5, 5]),
        ([4, 5], [5, 5], [5, 5]),
        ([5, 6], [5, 5], [5, 5]),
        ([5, 4], [5, 5], [5, 5]),
        ([6, 6], [5, 5], [5, 5]),
        ([6, 4], [5, 5], [5, 5]),
        ([4, 6], [5, 5], [5, 5]),
        ([4, 4], [5, 5], [5, 5]),
        ([4, 7], [5, 5], [4, 6]),
        ([5, 7], [5, 5], [5, 6]),
        ([6, 7], [5, 5], [6, 6]),
        ([7, 6], [5, 5], [6, 6]),
        ([7, 5], [5, 5], [6, 5]),
        ([7, 4], [5, 5], [6, 4]),
        ([6, 3], [5, 5], [6, 4]),
        ([5, 3], [5, 5], [5, 4]),
        ([4, 3], [5, 5], [4, 4]),
        ([3, 4], [5, 5], [4, 4]),
        ([3, 5], [5, 5], [4, 5]),
        ([3, 6], [5, 5], [4, 6]),
    ],
)
def test_follow(head, tail, expected_tail):
    follow(tail, head)
    assert tail[0] == expected_tail[0]
    assert tail[1] == expected_tail[1]
