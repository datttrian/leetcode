import pytest
from the_number_of_beautiful_subsets import Solution


@pytest.mark.parametrize(
    ["nums", "k", "expected"],
    [
        ([1, 2, 3], 1, 7),
        ([1, 2, 3], 2, 7),
        ([1, 5, 9], 4, 7),
        ([1, 1, 2], 1, 4),
    ],
)
def test_beautifulSubsets(nums: list[int], k: int, expected: int) -> None:
    solution = Solution()
    assert solution.beautifulSubsets(nums, k) == expected
