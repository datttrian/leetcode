from typing import List

import pytest
from insert_interval import Solution


@pytest.mark.parametrize(
    ('intervals', 'new_interval', 'expected'),
    [
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        (
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [4, 8],
            [[1, 2], [3, 10], [12, 16]],
        ),
        ([[1, 3], [6, 9]], [8, 10], [[1, 3], [6, 10]]),
        (
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [0, 2],
            [[0, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
        ),
        (
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [17, 18],
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16], [17, 18]],
        ),
        ([], [5, 7], [[5, 7]]),
    ],
)
def test_insert(
    intervals: List[List[int]],
    new_interval: List[int],
    expected: List[List[int]],
):
    solution = Solution()
    result = solution.insert(intervals, new_interval)
    assert result == expected
