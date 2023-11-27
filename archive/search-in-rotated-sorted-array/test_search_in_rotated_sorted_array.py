from typing import List

import pytest
from search_in_rotated_sorted_array import Solution


@pytest.mark.parametrize(
    ('nums', 'target', 'expected_result'),
    [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([4, 5, 6, 7, 8, 1, 2, 3], 8, 4),
        ([3, 1], 1, 1),
        ([1, 3], 0, -1),
        ([5, 1, 3], 5, 0),
        ([3, 5, 1], 1, 2),
        ([4, 5, 6, 7, 8, 1, 2, 3], 3, 7),
        ([1, 2, 3, 4, 5, 6], 4, 3),
        ([5, 1, 2, 3, 4], 1, 1),
        ([2, 3, 4, 5, 1], 1, 4),
    ],
)
def test_search(nums: List[int], target: int, expected_result: int):
    solution = Solution()
    result = solution.search(nums, target)
    assert result == expected_result
