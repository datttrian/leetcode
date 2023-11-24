from typing import List
import pytest
from first_missing_positive import Solution


@pytest.mark.parametrize(
    ('nums', 'expected_output'),
    [
        ([1, 2, 0], 3),
        ([3, 4, -1, 1], 2),
        ([7, 8, 9, 11, 12], 1),
        # Add more test cases as needed
    ],
)
def test_firstMissingPositive(nums: List[int], expected_output: int):
    solution = Solution()
    result = solution.firstMissingPositive(nums)
    assert result == expected_output
