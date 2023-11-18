import pytest
from divide_two_integers import Solution


@pytest.mark.parametrize(
    ('dividend', 'divisor', 'expected_result'),
    [
        (10, 3, 3),
        (7, -3, -2),
        (-2147483648, -1, 2147483647),
        (0, 1, 0),
        (1, 1, 1),
        # (-2147483648, 2, -1073741824),
        (2147483647, 1, 2147483647),
        (-2147483648, -3, 715827882),
    ],
)
def test_divide(dividend: int, divisor: int, expected_result: int):
    solution = Solution()
    result = solution.divide(dividend, divisor)
    assert result == expected_result
