from typing import List
import pytest
from remove_duplicates_from_sorted_array import Solution


@pytest.mark.parametrize(
    ('nums', 'expected_result', 'expected_nums'),
    [
        ([], 0, []),
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        ([1, 2, 3], 3, [1, 2, 3]),
        ([1, 1, 1, 1], 1, [1]),
        ([1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5], 5, [1, 2, 3, 4, 5]),
    ],
)
def test_removeDuplicates(
    nums: List[int],
    expected_result: int,
    expected_nums: List[int],
):
    solution = Solution()
    result = solution.removeDuplicates(nums)
    assert result == expected_result
    assert nums[:result] == expected_nums
