import pytest
from permutation_sequence import Solution


@pytest.mark.parametrize(
    ('n', 'k', 'expected'),
    [
        (3, 3, '213'),
        (4, 9, '2314'),
        (1, 1, '1'),
        (2, 2, '21'),
        # (5, 24, '54321'),
        (3, 5, '312'),
        # (4, 18, '3412'),
    ],
)
def test_getPermutation(n: int, k: int, expected: str):
    solution = Solution()
    result = solution.getPermutation(n, k)
    assert result == expected
