from typing import List

import pytest
from search_insert_position import Solution


@pytest.mark.parametrize(
    ('nums', 'target', 'expected_result'),
    [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 0, 0),
        ([], 7, 0),
        ([1], 0, 0),
        ([1], 2, 1),
        ([1, 2, 3, 4, 5, 6], 4, 3),
        ([1, 2, 4, 5, 6], 3, 2),
        ([1, 2, 4, 5, 6], 7, 5),
        ([1, 3, 5, 6], 4, 2),
    ],
)
def test_searchInsert(nums: List[int], target: int, expected_result: int):
    solution = Solution()
    result = solution.searchInsert(nums, target)
    assert result == expected_result
