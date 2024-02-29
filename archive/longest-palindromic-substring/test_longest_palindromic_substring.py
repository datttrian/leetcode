import pytest
from longest_palindromic_substring import Solution


class TestSolution:
    @pytest.mark.parametrize(
        ('input_str', 'expected_output'),
        [
            ('babad', 'bab'),
            ('ac', 'a'),
            ('cbbd', 'bb'),
            ('a', 'a'),
            ('abcda', 'a'),
            ('abcdefedcba', 'abcdefedcba'),
        ],
    )
    def test_longestPalindrome(self, input_str: str, expected_output: str):
        solution = Solution()
        assert solution.longestPalindrome(input_str) == expected_output
