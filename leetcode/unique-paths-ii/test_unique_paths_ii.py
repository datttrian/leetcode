from typing import List
import pytest
from unique_paths_ii import Solution


@pytest.mark.parametrize(
    ('obstacleGrid', 'expected'),
    [
        (
            [
                [0, 0, 0],
                [0, 1, 0],
                [0, 0, 0],
            ],
            2,
        ),
        (
            [
                [0, 1],
                [0, 0],
            ],
            1,
        ),
        (
            [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ],
            6,
        ),
        (
            [
                [1, 0],
                [0, 0],
            ],
            0,
        ),
        (
            [
                [0, 0],
                [0, 1],
            ],
            0,
        ),
        (
            [
                [0, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
            ],
            0,
        ),
        # (
        #     [
        #         [0, 0, 0],
        #         [0, 0, 0],
        #         [0, 1, 0],
        #     ],
        #     4,
        # ),
    ],
)
def test_uniquePathsWithObstacles(
    obstacleGrid: List[List[int]],
    expected: int,
):
    solution = Solution()
    result = solution.uniquePathsWithObstacles(obstacleGrid)
    assert result == expected
