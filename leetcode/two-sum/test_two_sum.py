import pytest
from two_sum import Solution


@pytest.mark.parametrize(
    ('nums', 'target', 'expected'),
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_two_sum(nums: list[int], target: int, expected: list[int]) -> None:
    solution = Solution()
    assert solution.twoSum(nums, target) == expected
