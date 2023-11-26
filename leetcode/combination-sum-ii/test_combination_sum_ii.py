from typing import List

import pytest
from combination_sum_ii import Solution


@pytest.mark.parametrize(
    ('candidates', 'target', 'expected_output'),
    [
        ([10, 1, 2, 7, 6, 1, 5], 8, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
        ([2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]]),
        # Add more test cases as needed
    ],
)
def test_combinationSum2(
    candidates: List[int],
    target: int,
    expected_output: List[List[int]],
):
    solution = Solution()
    result = solution.combinationSum2(candidates, target)
    assert result == expected_output


# Run the tests
if __name__ == '__main__':
    pytest.main()
