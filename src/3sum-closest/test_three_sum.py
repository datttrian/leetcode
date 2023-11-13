from typing import List, Tuple
import pytest
from three_sum import Solution


@pytest.mark.parametrize(
    ('nums', 'expected'),
    [
        ([], []),
        ([0, 0, 0], [(0, 0, 0)]),
        ([-1, 0, 1, 2, -1, -4], [(-1, -1, 2), (-1, 0, 1)]),
        ([-1, 2, 1, -4], []),
        ([1, 2, -2, -1], []),
        ([1, 2, 3], []),
        ([1, 1, -2], [(-2, 1, 1)]),
        ([3, 0, -2, -1, 1, 2], [(-2, -1, 3), (-2, 0, 2), (-1, 0, 1)]),
        ([1, 1, 1, 1], []),
    ],
)
def test_threeSum(nums: List[int], expected: List[Tuple[int, int, int]]):
    solution = Solution()
    assert solution.threeSum(nums) == expected