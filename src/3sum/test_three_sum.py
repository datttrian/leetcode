from typing import List, Tuple
import pytest
from three_sum import (
    Solution,
)  # Assuming your solution class is in a module called solution_module


@pytest.mark.parametrize(
    ('nums', 'expected'),
    [
        # ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([], []),
        ([0], []),
        ([1, 2], []),
        # ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
        # ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),
    ],
)
def test_threeSum(nums: List[int], expected: List[Tuple[int, int, int]]):
    solution = Solution()
    assert solution.threeSum(nums) == expected
