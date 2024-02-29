import pytest
from unique_paths import Solution


@pytest.mark.parametrize(
    ('m', 'n', 'expected'),
    [
        (3, 7, 28),
        (3, 2, 3),
        (7, 3, 28),
        (3, 3, 6),
        (1, 1, 1),
        (1, 10, 1),
        (10, 1, 1),
        (2, 2, 2),
        (4, 4, 20),
    ],
)
def test_uniquePaths(m: int, n: int, expected: int):
    solution = Solution()
    result = solution.uniquePaths(m, n)
    assert result == expected
