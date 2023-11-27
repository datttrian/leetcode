import pytest
from combinations_ import Solution


@pytest.mark.parametrize(
    ('n', 'k', 'expected'),
    [
        (4, 2, [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]),
        (1, 1, [[1]]),
        (
            5,
            3,
            [
                [1, 2, 3],
                [1, 2, 4],
                [1, 2, 5],
                [1, 3, 4],
                [1, 3, 5],
                [1, 4, 5],
                [2, 3, 4],
                [2, 3, 5],
                [2, 4, 5],
                [3, 4, 5],
            ],
        ),
    ],
)
def test_combine(n: int, k: int, expected: list[list[int]]):
    solution = Solution()
    result = solution.combine(n, k)
    assert result == expected
