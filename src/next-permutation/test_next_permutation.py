import pytest
from next_permutation import Solution
from typing import List


@pytest.mark.parametrize(
    ('nums', 'expected_result'),
    [
        ([1, 2, 3], [1, 3, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 1, 5], [1, 5, 1]),
        ([1], [1]),
        ([1, 3, 2], [2, 1, 3]),
        ([2, 3, 1], [3, 1, 2]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 5, 4]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        # ([1, 3, 5, 4, 2], [2, 1, 3, 4, 5]),
    ],
)
def test_nextPermutation(nums: List[int], expected_result: List[int]):
    solution = Solution()
    solution.nextPermutation(nums)
    assert nums == expected_result
