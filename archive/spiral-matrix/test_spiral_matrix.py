from typing import List

import pytest
from spiral_matrix import Solution


@pytest.mark.parametrize(
    ('matrix', 'expected'),
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        ),
        ([[1, 2, 3], [4, 5, 6]], [1, 2, 3, 6, 5, 4]),
        ([], []),
        ([[1]], [1]),
        ([[1, 2, 3, 4]], [1, 2, 3, 4]),
    ],
)
def test_spiralOrder(matrix: List[List[int]], expected: List[int]):
    solution = Solution()
    result = solution.spiralOrder(matrix)
    assert result == expected
