from typing import List
import pytest
from minimum_path_sum import Solution


@pytest.mark.parametrize(
    ('grid', 'expected'),
    [
        (
            [
                [1, 3, 1],
                [1, 5, 1],
                [4, 2, 1],
            ],
            7,
        ),
        (
            [
                [1, 2, 3],
                [4, 5, 6],
            ],
            12,
        ),
        # (
        #     [
        #         [1, 2],
        #         [5, 6],
        #         [1, 1],
        #     ],
        #     7,
        # ),
        # (
        #     [
        #         [2, 3, 4],
        #         [0, 1, 2],
        #         [1, 4, 1],
        #     ],
        #     7,
        # ),
        (
            [
                [1, 2, 5],
                [3, 2, 1],
            ],
            6,
        ),
        (
            [
                [1],
            ],
            1,
        ),
    ],
)
def test_minPathSum(grid: List[List[int]], expected: int):
    solution = Solution()
    result = solution.minPathSum(grid)
    assert result == expected
