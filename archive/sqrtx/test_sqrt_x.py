import pytest
from sqrt_x import Solution


@pytest.mark.parametrize(
    ('x', 'expected'),
    [
        (4, 2),
        (8, 2),  # Floor of the square root of 8 is 2
        (0, 0),
        (1, 1),
        (16, 4),
        (25, 5),
        (30, 5),  # Floor of the square root of 30 is 5
        (100, 10),
    ],
)
def test_mySqrt(x: int, expected: int):
    solution = Solution()
    result = solution.mySqrt(x)
    assert result == expected
