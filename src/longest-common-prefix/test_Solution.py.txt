import pytest
from longest_common_prefix.Solution import Solution  # Assuming your solution is in a module named solution_module

class TestSolution:
    @pytest.mark.parametrize("input_strs, expected_output", [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["apple", "appetizer", "apartment"], "ap"),
        (["abc", "abcd", "abcde"], "abc"),
        (["abc", "def", "ghi"], ""),
    ])
    def test_longestCommonPrefix(self, input_strs, expected_output):
        solution = Solution()
        assert solution.longestCommonPrefix(input_strs) == expected_output
