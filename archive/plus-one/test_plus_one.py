from typing import List

import pytest
from plus_one import Solution


@pytest.mark.parametrize(
    ('digits', 'expected'),
    [
        ([1, 2, 3], [1, 2, 4]),
        ([4, 3, 2, 1], [4, 3, 2, 2]),
        ([9], [1, 0]),
        ([9, 9, 9], [1, 0, 0, 0]),
        ([0], [1]),
        ([5, 6, 7, 8, 9], [5, 6, 7, 9, 0]),
    ],
)
def test_plusOne(digits: List[int], expected: List[int]):
    solution = Solution()
    result = solution.plusOne(digits)
    assert result == expected
