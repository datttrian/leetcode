import pytest
from search_in_rotated_sorted_array_ii import Solution


@pytest.mark.parametrize(
    ('nums', 'target', 'expected_result'),
    [
        # Test cases with rotated sorted arrays
        ([2, 5, 6, 0, 0, 1, 2], 0, True),
        ([2, 5, 6, 0, 0, 1, 2], 3, False),
        ([1, 3, 1, 1, 1], 3, True),
        ([1, 1, 1, 3, 1], 3, True),
        # Test cases with non-rotated sorted arrays
        ([1, 2, 3, 4, 5, 6], 4, True),
        ([1, 2, 3, 4, 5, 6], 0, False),
        ([1, 2, 3, 4, 5, 6], 7, False),
        # Test cases with empty arrays
        ([], 5, False),
    ],
)
def test_search(nums: list[int], target: int, expected_result: bool):
    solution = Solution()
    result = solution.search(nums, target)
    assert result == expected_result
