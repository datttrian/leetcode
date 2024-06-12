import pytest
from find_the_safest_path_in_a_grid import Solution


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[1, 0, 0], [0, 0, 0], [0, 0, 1]], 0),
        ([[0, 0, 1], [0, 0, 0], [0, 0, 0]], 2),
        ([[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]], 2),
        (
            [[1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]],
            0,
        ),
        ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 1),
        ([[0, 1, 0], [0, 1, 0], [0, 1, 0]], 0),
        (
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0],
            ],
            1,
        ),
        (
            [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]],
            1,
        ),
        (
            [
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
            ],
            3,
        ),
        ([[0, 0, 0], [1, 0, 1], [0, 0, 0]], 1),
    ],
)
def test_find_safest_path(grid: list[list[int]], expected: int) -> None:
    solution = Solution()
    assert solution.maximumSafenessFactor(grid) == expected
