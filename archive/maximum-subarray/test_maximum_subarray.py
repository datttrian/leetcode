from typing import List

import pytest
from maximum_subarray import Solution


@pytest.mark.parametrize(
    ('nums', 'expected'),
    [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
        ([-2, -1, -3, -4, -1, -2, -1, -5, -4], -1),
        ([], 0),
        ([-1, -2, -3, -4, -5], -1),
        ([10, -2, 5, 1, -1, 7, -2], 20),
        ([-1, 0, -2], 0),
    ],
)
def test_maxSubArray(nums: List[int], expected: int):
    solution = Solution()
    result = solution.maxSubArray(nums)
    assert result == expected
