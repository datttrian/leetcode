import pytest
from find_the_safest_path_in_a_grid import Solution


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[1, 0, 0], [0, 0, 0], [0, 0, 1]], 0),
        ([[0, 0, 1], [0, 0, 0], [0, 0, 0]], 2),
        ([[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]], 2),
        # Additional test cases
        (
            [[1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]],
            0,
        ),  # Surrounded by thieves
        ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 1),  # Single thief in the middle
        ([[0, 1, 0], [0, 1, 0], [0, 1, 0]], 0),  # Column of thieves
        (
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0],
            ],
            1,
        ),  # Square of thieves
        (
            [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]],
            1,
        ),  # Block of thieves in the middle
        (
            [
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
            ],
            3,
        ),  # Thieves in corners
        ([[0, 0, 0], [1, 0, 1], [0, 0, 0]], 1),  # Thieves on the border
        (
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]],
            3,
        ),  # One thief at the end
    ],
)
def test_find_safest_path(grid: list[list[int]], expected: int) -> None:
    solution = Solution()
    assert solution.maximumSafenessFactor(grid) == expected
