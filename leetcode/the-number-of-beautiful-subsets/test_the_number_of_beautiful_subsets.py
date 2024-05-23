import pytest
from the_number_of_beautiful_subsets import Solution


@pytest.mark.parametrize(
    ["nums", "k", "expected"],
    [
        ([1, 2, 3], 1, 4),
        ([], 1, 0),
        ([5], 3, 1),
        ([2, 2, 2], 1, 1),
        ([1, 2, 3, 4], 10, 15),
        (
            [1, 3, 5, 7],
            2,
            15,
        ),
        ([1, 1, 1], 0, 1),
        (
            [-3, -2, -1, 1, 2, 3],
            1,
            14,
        ),
        ([1, 2, 3, 4, 5, 6], 2, 32),
        ([4, 4, 5, 6, 7], 2, 16),
    ],
)
def test_beautifulSubsets(nums: list[int], k: int, expected: int) -> None:
    solution = Solution()
    assert solution.beautifulSubsets(nums, k) == expected
