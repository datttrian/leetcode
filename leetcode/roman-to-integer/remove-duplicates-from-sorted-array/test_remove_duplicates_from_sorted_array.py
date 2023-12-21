import pytest
from remove_duplicates_from_sorted_array import Solution


@pytest.mark.parametrize(
    ["nums", "expected"],
    [
        [[1, 1, 2], 2],  # Basic case with duplicate elements.
        [[0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5],  # Case with multiple duplicates.
        # [[], 0],  # Empty list case.
        [[1, 2, 3, 4], 4],  # Case with no duplicates.
        [[1, 1, 1, 1], 1],  # Case with all elements being duplicates.
    ],
)
def test_remove_duplicates(nums: list[int], expected: int) -> None:
    """Test the removeDuplicates function from the Solution class.

    Args:
    - nums (list[int]): Input list with duplicates.
    - expected (int): Expected length of the list after removing duplicates.

    Returns:
    - None
    """
    solution = Solution()
    result = solution.removeDuplicates(nums)
    assert result == expected
