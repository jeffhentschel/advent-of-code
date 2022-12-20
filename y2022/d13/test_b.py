import pytest

from .b import solve


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
            140,
        )
    ],
)
def test_solve(input, expected):
    answer = solve(input)
    assert answer == expected
