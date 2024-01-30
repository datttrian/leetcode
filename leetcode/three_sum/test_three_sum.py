import pytest
from three_sum import Solution


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([-1, 0, 1, 2, -1, -4], [(-1, -1, 2), (-1, 0, 1)]),
        ([], []),
        ([0], []),
        ([0, 0, 0], [(0, 0, 0)]),
    ],
)
def test_three_sum(
    nums: list[int], expected: list[tuple[int, int, int]]
) -> None:
    solution = Solution()
    result = solution.threeSum(nums)
    assert sorted(result) == sorted(expected)
