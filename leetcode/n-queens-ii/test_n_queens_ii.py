import pytest
from n_queens_ii import Solution


@pytest.mark.parametrize(
    ('n', 'expected'),
    [
        (4, 2),
        (1, 1),
        (2, 0),
        (8, 92),
    ],
)
def test_totalNQueens(n: int, expected: int):
    solution = Solution()
    result = solution.totalNQueens(n)
    assert result == expected
