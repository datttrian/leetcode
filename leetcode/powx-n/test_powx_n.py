import pytest
from powx_n import Solution


@pytest.mark.parametrize(
    ('x', 'n', 'expected'),
    [
        (2.0, 10, 1024.0),
        # (2.1, 3, 9.261),
        (2.0, -2, 0.25),
        (0.00001, 2147483647, 0.0),
        (2.0, 0, 1.0),
        (1.0, 1000000, 1.0),
        # (0.00001, -3, 1000000000000.0),
        (-2.0, 10, 1024.0),
        (-2.0, 9, -512.0),
    ],
)
def test_myPow(x: float, n: int, expected: float):
    solution = Solution()
    result = solution.myPow(x, n)
    # assert result == pytest.approx(expected, rel=1e-5)
    assert result == expected
