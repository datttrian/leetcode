import pytest
from the_number_of_beautiful_subsets import Solution


@pytest.mark.parametrize(
    ["nums", "k", "expected"],
    [
        ([1, 2, 3], 1, 4),
        ([], 1, 0),
        ([5], 3, 1),
        ([1, 2, 3, 4], 10, 15),
        ([2, 4, 6], 2, 4),
        ([10, 20, 30], 15, 7),
    ],
)
def test_beautifulSubsets(nums: list[int], k: int, expected: int) -> None:
    solution = Solution()
    assert solution.beautifulSubsets(nums, k) == expected
