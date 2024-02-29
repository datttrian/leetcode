from typing import List

import pytest
from spiral_matrix_ii import Solution


@pytest.mark.parametrize(
    ('n', 'expected'),
    [
        (3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]]),
        (1, [[1]]),
        (4, [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]),
        (2, [[1, 2], [4, 3]]),
        (
            5,
            [
                [1, 2, 3, 4, 5],
                [16, 17, 18, 19, 6],
                [15, 24, 25, 20, 7],
                [14, 23, 22, 21, 8],
                [13, 12, 11, 10, 9],
            ],
        ),
    ],
)
def test_generateMatrix(n: int, expected: List[int]):
    solution = Solution()
    result = solution.generateMatrix(n)
    assert result == expected
