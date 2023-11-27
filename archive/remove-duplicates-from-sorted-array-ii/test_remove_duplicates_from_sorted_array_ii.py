import pytest
from remove_duplicates_from_sorted_array_ii import Solution


@pytest.mark.parametrize(
    ('input_nums', 'expected_length', 'expected_result'),
    [
        # Test cases with duplicates
        ([1, 1, 1, 2, 2, 3], 5, [1, 1, 2, 2, 3]),
        ([0, 0, 1, 1, 1, 1, 2, 3, 3], 7, [0, 0, 1, 1, 2, 3, 3]),
        # ([-1, -1, 0, 0, 0, 1, 1, 1, 1, 1], 8, [-1, -1, 0, 0, 1, 1, 1, 1, 1]),
        # Test cases with no duplicates
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
        ([-1, 0, 1, 2, 3], 5, [-1, 0, 1, 2, 3]),
        # Test cases with empty arrays
        ([], 0, []),
    ],
)
def test_removeDuplicates(
    input_nums: list[int],
    expected_length: int,
    expected_result: list[int],
):
    solution = Solution()
    result = solution.removeDuplicates(input_nums)
    assert result == expected_length
    assert input_nums[:result] == expected_result
