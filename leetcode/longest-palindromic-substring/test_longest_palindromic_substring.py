import pytest
from longest_palindromic_substring import Solution


class TestSolution:
    @pytest.mark.parametrize(
        ("input_str", "expected_output"),
        [
            ("babad", "bab"),
            ("ac", "a"),
            ("cbbd", "bb"),
            ("a", "a"),
            ("abcda", "a"),
            ("abcdefedcba", "abcdefedcba"),
        ],
    )
    def test_longest_palindromic_substring(
        self, input_str: str, expected_output: str
    ) -> None:
        solution = Solution()
        assert solution.longestPalindrome(input_str) == expected_output
