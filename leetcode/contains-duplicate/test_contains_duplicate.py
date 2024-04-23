import pytest
from contains_duplicate import Solution


@pytest.mark.parametrize(
    ["input_nums", "expected"],
    [
        [[1, 2, 3, 1], True],
        [[1, 2, 3, 4], False],
        [[1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True],
    ],
)
def test_contains_duplicate(input_nums: list[int], expected: bool) -> None:
    solution = Solution()
    assert solution.containsDuplicate(input_nums) == expected
