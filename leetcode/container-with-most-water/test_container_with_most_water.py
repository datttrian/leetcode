import pytest
from container_with_most_water import Solution


@pytest.mark.parametrize(
    ["height", "expected"],
    [
        [
            [1, 8, 6, 2, 5, 4, 8, 3, 7],
            49,
        ],  # Basic case with a container that can hold the most water.
        [[1, 1], 1],  # Basic case with a container of smaller size.
        [
            [4, 3, 2, 1, 4],
            16,
        ],  # Another basic case with a container that can hold the most water.
        [[1, 2, 1], 2],  # Case with a smaller container in the middle.
        [
            [2, 3, 4, 5, 18, 17, 6],
            17,
        ],  # Case with an irregular arrangement of containers.
        [[2, 1, 8, 1, 2], 8],  # Case with a larger container in the middle.
        [[1, 2, 3, 4, 5], 6],  # Case with increasing heights.
        [[5, 4, 3, 2, 1], 6],  # Case with decreasing heights.
        [[], 0],  # Empty list case.
        [[1], 0],  # List with only one element.
    ],
)
def test_container_with_most_water(height: list[int], expected: int) -> None:
    container = Solution()
    result = container.maxArea(height)
    assert result == expected
