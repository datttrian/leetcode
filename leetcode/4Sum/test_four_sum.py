from typing import List
import pytest
from four_sum import Solution


@pytest.mark.parametrize(
    ('nums', 'target', 'expected'),
    [
        ([], 0, []),
        (
            [1, 0, -1, 0, -2, 2],
            0,
            [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]],
        ),
        ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
        ([-1, 0, 1, 2, -1, -4], -1, [[-4, 0, 1, 2], [-1, -1, 0, 1]]),
        ([1, 2, 3, 4, 5], 10, [[1, 2, 3, 4]]),
        # ([-1, 0, 1, 2, -1, -4], 1, [[-4, 0, 1, 2]]),
        ([0, 0, 0, 0], 0, [[0, 0, 0, 0]]),
    ],
)
def test_fourSum(nums: List[int], target: int, expected: List[List[int]]):
    solution = Solution()
    assert solution.fourSum(nums, target) == expected
