import pytest
from subsets_ import Solution


@pytest.mark.parametrize(
    ('nums', 'expected'),
    [
        ([1, 2, 3], [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]),
        ([1], [[], [1]]),
        # ([], [[]]),
        ([4, 5, 6], [[], [4], [4, 5], [4, 5, 6], [4, 6], [5], [5, 6], [6]]),
    ],
)
def test_subsets(nums: list[int], expected: list[list[int]]):
    solution = Solution()
    result = solution.subsets(nums)
    assert result == expected
