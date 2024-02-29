import pytest
from largest_rectangle_in_histogram import Solution


@pytest.mark.parametrize(
    ('heights', 'expected_result'),
    [
        # Test case with ascending heights
        ([1, 2, 3, 4, 5], 9),
        # Test case with descending heights
        ([5, 4, 3, 2, 1], 9),
        # Test case with random heights
        ([2, 1, 5, 6, 2, 3], 10),
        # Test case with all heights being the same
        ([3, 3, 3, 3, 3], 15),
        # Test case with an empty list
        ([], 0),
    ],
)
def test_largestRectangleArea(heights: list[int], expected_result: int):
    solution = Solution()
    result = solution.largestRectangleArea(heights)
    assert result == expected_result
