import pytest
from score_after_flipping_matrix import Solution


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]], 39),
        ([[0]], 1),
        ([[0, 0, 0], [0, 1, 1], [1, 0, 0]], 18),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 21),
        ([[1]], 1),
    ],
)
def test_matrix_score(grid: list[list[int]], expected: int) -> None:
    solution = Solution()
    assert solution.matrixScore(grid) == expected
