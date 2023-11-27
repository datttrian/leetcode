import pytest
from sort_colors import Solution


@pytest.mark.parametrize(
    ('nums', 'expected'),
    [
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2]),
        ([0], [0]),
        ([1], [1]),
        ([2, 1, 0], [0, 1, 2]),
        ([1, 0, 2], [0, 1, 2]),
    ],
)
def test_sortColors(nums: list[int], expected: list[int]):
    solution = Solution()
    solution.sortColors(nums)
    assert nums == expected
