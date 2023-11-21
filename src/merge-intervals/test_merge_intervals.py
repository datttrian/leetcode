from typing import List
import pytest
from merge_intervals import Solution


@pytest.mark.parametrize(
    ('intervals', 'expected'),
    [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([[1, 4], [0, 4]], [[0, 4]]),
        ([[1, 4], [2, 3]], [[1, 4]]),
        ([[1, 4], [0, 2], [3, 5]], [[0, 5]]),
        ([], []),
        ([[1, 3], [4, 5], [6, 7], [8, 9]], [[1, 3], [4, 5], [6, 7], [8, 9]]),
    ],
)
def test_merge(intervals: List[List[int]], expected: List[List[int]]):
    solution = Solution()
    result = solution.merge(intervals)
    assert result == expected
