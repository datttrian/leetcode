import pytest
from median_of_two_sorted_arrays import Solution
from typing import List


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    ('a', 'b', 'expected_median'),
    [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([0, 0], [0, 0], 0.0),
        ([], [1], 1.0),
        ([2], [], 2.0),
        ([], [], None),
    ],
)
def test_find_median_sorted_arrays(
    solution, a: List[int], b: List[int], expected_median: float
):
    result = solution.findMedianSortedArrays(a, b)
    assert result == expected_median
