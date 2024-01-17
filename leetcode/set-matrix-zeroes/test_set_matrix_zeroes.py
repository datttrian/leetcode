import pytest
from set_matrix_zeroes import Solution


@pytest.mark.parametrize(
    ("matrix", "expected"),
    [
        (
            [
                [1, 2, 3],
                [4, 0, 6],
                [7, 8, 9],
            ],
            [
                [1, 0, 3],
                [0, 0, 0],
                [7, 0, 9],
            ],
        ),
        (
            [
                [0, 1, 2, 0],
                [3, 4, 5, 2],
                [1, 3, 1, 5],
            ],
            [
                [0, 0, 0, 0],
                [0, 4, 5, 0],
                [0, 3, 1, 0],
            ],
        ),
        (
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 0],
            ],
            [
                [1, 2, 0],
                [4, 5, 0],
                [0, 0, 0],
            ],
        ),
        (
            [
                [1, 0],
                [1, 1],
            ],
            [
                [0, 0],
                [1, 0],
            ],
        ),
        (
            [
                [0],
            ],
            [
                [0],
            ],
        ),
        (
            [
                [1],
            ],
            [
                [1],
            ],
        ),
        (
            [
                [0, 0],
            ],
            [
                [0, 0],
            ],
        ),
    ],
)
def test_set_matrix_zeroes(
    matrix: list[list[int]], expected: list[list[int]]
) -> None:
    solution = Solution()
    solution.setZeroes(matrix)
    assert matrix == expected
