import pytest
from longest_substring_without_repeating_characters import Solution


class TestSolution:
    @pytest.mark.parametrize(
        ('s', 'expected'),
        [
            ('abcabcbb', 3),
            ('bbbbb', 1),
            ('pwwkew', 3),
            ('', 0),
            ('abcdefg', 7),
            ('aab', 2),
            ('dvdf', 3),
        ],
    )
    def test_lengthOfLongestSubstring(self, s: str, expected: int):
        solution = Solution()
        assert solution.lengthOfLongestSubstring(s) == expected