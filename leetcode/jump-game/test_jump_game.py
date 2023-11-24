from typing import List
import pytest
from jump_game import Solution


@pytest.mark.parametrize(
    ('nums', 'expected'),
    [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([0], True),
        ([1, 2, 3], True),
        ([4, 0, 0, 0, 0], True),
        ([0, 0, 0, 0, 1], False),
        ([1, 0, 0, 0, 0], False),
        ([1, 1, 1, 1, 0], True),
        ([1, 0, 1, 0, 1], False),
        ([5, 0, 0, 0, 0], True),
    ],
)
def test_canJump(nums: List[int], expected: bool):
    solution = Solution()
    result = solution.canJump(nums)
    assert result == expected
