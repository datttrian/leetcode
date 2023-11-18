from typing import List
import pytest
from remove_element import Solution


@pytest.mark.parametrize(
    ('nums', 'val', 'expected_result', 'expected_nums'),
    [
        ([], 1, 0, []),
        ([1, 2, 3, 4], 5, 4, [1, 2, 3, 4]),
        ([3, 2, 2, 3], 3, 2, [2, 2]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 3, 0, 4]),
        ([1, 1, 1, 1], 1, 0, []),
        ([7, 7, 7, 7], 7, 0, []),
    ],
)
def test_removeElement(
    nums: List[int],
    val: int,
    expected_result: int,
    expected_nums: List[int],
):
    solution = Solution()
    result = solution.removeElement(nums, val)
    assert result == expected_result
    assert nums[:result] == expected_nums
