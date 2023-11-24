import pytest
from search_a_2d_matrix import Solution


@pytest.mark.parametrize(
    ('matrix', 'target', 'expected'),
    [
        # (
        #     [
        #         [1, 4, 7, 11],
        #         [2, 5, 8, 12],
        #         [3, 6, 9, 16],
        #         [10, 13, 14, 17],
        #     ],
        #     5,
        #     True,
        # ),
        (
            [
                [1, 4, 7, 11],
                [2, 5, 8, 12],
                [3, 6, 9, 16],
                [10, 13, 14, 17],
            ],
            20,
            False,
        ),
        (
            [
                [1, 3, 5, 7],
                [10, 11, 16, 20],
                [23, 30, 34, 60],
            ],
            3,
            True,
        ),
        (
            [
                [1, 3, 5, 7],
                [10, 11, 16, 20],
                [23, 30, 34, 60],
            ],
            13,
            False,
        ),
        (
            [
                [1],
            ],
            1,
            True,
        ),
        (
            [
                [1],
            ],
            2,
            False,
        ),
        (
            [
                [1, 3, 5, 7],
            ],
            4,
            False,
        ),
        (
            [],
            4,
            False,
        ),
    ],
)
def test_searchMatrix(matrix: list[list[int]], target: int, expected: bool):
    solution = Solution()
    result = solution.searchMatrix(matrix, target)
    assert result == expected
