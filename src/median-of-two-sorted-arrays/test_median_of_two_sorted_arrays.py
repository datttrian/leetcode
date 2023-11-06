import pytest
from median_of_two_sorted_arrays import Solution
from typing import List, Optional


@pytest.mark.parametrize(
    ('a', 'b', 'expected_median'),
    [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([0, 0], [0, 0], 0.0),
        ([], [1], 1.0),
        ([2], [], 2.0),
        (
            [],
            [],
            None,
        ),  # This case needs special handling in the function itself.
    ],
)
def test_findMedianSortedArrays(
    solution: Solution,
    a: List[int],
    b: List[int],
    expected_median: Optional[float],
) -> None:
    solution = Solution()
    result = solution.findMedianSortedArrays(a, b)
    assert result == expected_median
