from typing import List

import pytest
from permutations_i import Solution


@pytest.mark.parametrize(
    ('nums', 'expected'),
    [
        (
            [1, 2, 3],
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]],
        ),
        # ([], [[]]),
        ([1], [[1]]),
        ([1, 2], [[1, 2], [2, 1]]),
        (
            [1, 2, 3, 4],
            [
                [1, 2, 3, 4],
                [1, 2, 4, 3],
                [1, 3, 2, 4],
                [1, 3, 4, 2],
                [1, 4, 3, 2],
                [1, 4, 2, 3],
                [2, 1, 3, 4],
                [2, 1, 4, 3],
                [2, 3, 1, 4],
                [2, 3, 4, 1],
                [2, 4, 3, 1],
                [2, 4, 1, 3],
                [3, 2, 1, 4],
                [3, 2, 4, 1],
                [3, 1, 2, 4],
                [3, 1, 4, 2],
                [3, 4, 1, 2],
                [3, 4, 2, 1],
                [4, 2, 3, 1],
                [4, 2, 1, 3],
                [4, 3, 2, 1],
                [4, 3, 1, 2],
                [4, 1, 3, 2],
                [4, 1, 2, 3],
            ],
        ),
    ],
)
def test_permute(nums: List[int], expected: List[List[int]]):
    solution = Solution()
    assert solution.permute(nums) == expected
