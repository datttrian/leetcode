import pytest
from largest_positive_integer_that_exists_with_its_negative import Solution


@pytest.mark.parametrize(
    "nums, expected_result",
    [
        ([], -1),
        ([1, 2, 3, 4], -1),
        ([-1, -2, -3, -4], -1),
        ([1, 2, 3, -4], -1),
        ([1, 2, 3, 0], -1),
        ([0, 0, 0, 0], -1),
        ([1, -1, 1, -1], 1),
        ([1, 1, 1, -1], 1),
    ],
)
def test_findMaxK(nums: list[int], expected_result: int) -> None:
    solution = Solution()
    assert solution.findMaxK(nums) == expected_result
