import pytest

from .a import is_valid, solve


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("[1,1,3,1,1]", "[1,1,5,1,1]", True),
        ("[[1],[2,3,4]]", "[[1],4]", True),
        ("[9]", "[[8,7,6]]", False),
        ("[[4,4],4,4]", "[[4,4],4,4,4]", True),
        ("[7,7,7,7]", "[7,7,7]", False),
        ("[]", "[3]", True),
        ("[[[]]]", "[[]]", False),
        ("[1,[2,[3,[4,[5,6,7]]]],8,9]", "[1,[2,[3,[4,[5,6,0]]]],8,9]", False),
    ],
)
def test_is_valid(a, b, expected):
    answer = is_valid(a, b)
    assert answer == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        (
            """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""",
            13,
        )
    ],
)
def test_solve(input, expected):
    answer = solve(input)
    assert answer == expected
