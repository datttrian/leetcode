import pytest
from climbing_stairs import Solution


@pytest.mark.parametrize(
    ('n', 'expected'),
    [
        # 1 step + 1 step + 1 step or 1 step + 2 steps
        (1, 1),
        (2, 2),
        (3, 3),
        # 1 step + 1 step + 1 step + 1 step or 1 step + 2 steps + 1 step or 2
        # steps + 1 step + 1 step or 2 steps + 2 steps
        (
            4,
            5,
        ),
        # 1 + 1 + 1 + 1 + 1 or 1 + 1 + 1 + 2 or 1 + 1 + 2 + 1 or 1 + 2 + 1 + 1
        # or 2 + 1 + 1 + 1 or 2 + 2 + 1 or 2 + 1 + 2 or 1 + 2 + 2
        (
            5,
            8,
        ),
        (10, 89),  # Number of ways to climb a staircase with 10 steps
    ],
)
def test_climbStairs(n: int, expected: int):
    solution = Solution()
    result = solution.climbStairs(n)
    assert result == expected
