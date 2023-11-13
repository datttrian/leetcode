from typing import List
import pytest
from three_sum_closest import Solution


class TestSolution:
    @pytest.mark.parametrize(
        ('nums', 'target', 'expected'),
        [
            ([-1, 2, 1, -4], 1, 2),
            ([0, 0, 0], 1, 0),
            ([1, 2, 3], 6, 6),
            ([-10, -5, 0, 5, 10], 1, 0),
            ([1, 1, 1, 1], 4, 3),
        ],
    )
    def test_threeSumClosest(
        self,
        nums: List[int],
        target: int,
        expected: int,
    ):
        solution = Solution()
        result = solution.threeSumClosest(nums, target)
        assert result == expected
