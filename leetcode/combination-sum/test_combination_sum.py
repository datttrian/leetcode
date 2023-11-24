from typing import List
import pytest
from combination_sum import Solution


@pytest.mark.parametrize(
    ('candidates', 'target', 'expected_output'),
    [
        ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
        ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        # Add more test cases as needed
    ],
)
def test_combinationSum(
    candidates: List[int],
    target: int,
    expected_output: List[List[int]],
):
    solution = Solution()
    result = solution.combinationSum(candidates, target)
    assert result == expected_output
