import pytest
from typing import List
from two_sum import Solution


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        # Add more test cases here
    ],
)
def test_twoSum(nums: List[int], target: int, expected: List[int]):
    solution = Solution()
    assert solution.twoSum(nums, target) == expected
