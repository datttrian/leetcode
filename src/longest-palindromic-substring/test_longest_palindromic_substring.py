import pytest
from longest_palindromic_substring import Solution


class TestSolution:
    @pytest.mark.parametrize(
        "input_str, expected_output",
        [
            ("babad", "bab"),
            ("cbbd", "bb"),
            ("a", "a"),
            ("ac", "a"),
            ("abcda", "a"),
            ("abcdefedcba", "abcdefedcba"),
        ],
    )
    def test_longestPalindrome(self, input_str, expected_output):
        solution = Solution()
        assert solution.longestPalindrome(input_str) == expected_output
