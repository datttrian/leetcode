import pytest
from typing import List
from remove_duplicates_from_sorted_array.Solution import Solution


class TestSolution:
    @pytest.mark.parametrize(
        "input_nums, expected_result",
        [
            ([1, 1, 2], [1, 2]),
            ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([1, 1, 1, 1, 1, 1, 1], [1]),
            ([], []),
            ([1, 2, 2, 3, 3, 4, 4, 5, 5], [1, 2, 3, 4, 5]),
        ],
    )
    def test_remove_duplicates(self, input_nums, expected_result):
        solution = Solution()
        result = solution.removeDuplicates(input_nums)
        assert result == len(expected_result)
        assert input_nums[: len(expected_result)] == expected_result
