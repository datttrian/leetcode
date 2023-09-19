import pytest
from next_permutation import (
    Solution,
)  # Import the Solution class from your implementation


class TestSolution:
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 3], [1, 3, 2]),
            ([3, 2, 1], [1, 2, 3]),
            ([1, 1, 5], [1, 5, 1]),
            ([1], [1]),
            ([1, 3, 2], [2, 1, 3]),
            ([3, 1, 2], [3, 2, 1]),
            ([1, 2, 3, 4], [1, 2, 4, 3]),
            ([4, 3, 2, 1], [1, 2, 3, 4]),
            ([1, 2, 2], [2, 1, 2]),
            ([1, 1], [1, 1]),
        ],
    )
    def test_nextPermutation(self, nums, expected):
        solution = Solution()
        solution.nextPermutation(nums)
        assert nums == expected

    def test_emptyList(self):
        solution = Solution()
        nums = []
        expected = []
        solution.nextPermutation(nums)
        assert nums == expected
