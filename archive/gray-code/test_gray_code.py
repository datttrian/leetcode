import pytest
from gray_code import Solution


@pytest.mark.parametrize(
    ('n', 'expected_result'),
    [
        (2, [0, 1, 3, 2]),
        (3, [0, 1, 3, 2, 6, 7, 5, 4]),
        (1, [0, 1]),
        (4, [0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8]),
        # Add more test cases as needed
    ],
)
def test_grayCode(n: int, expected_result: list[int]):
    solution = Solution()
    result = solution.grayCode(n)
    assert result == expected_result
