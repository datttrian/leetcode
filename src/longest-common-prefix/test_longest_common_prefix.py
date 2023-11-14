import pytest
from longest_common_prefix import Solution
from typing import List


@pytest.mark.parametrize(
    ('input_strs', 'expected_output'),
    [
        (['flower', 'flow', 'flight'], 'fl'),
        (['dog', 'racecar', 'car'], ''),
        (['apple', 'appetizer', 'apartment'], 'ap'),
        (['abc', 'abcd', 'abcde'], 'abc'),
        (['abc', 'def', 'ghi'], ''),
    ],
)
def test_longestCommonPrefix(input_strs: List[str], expected_output: str):
    solution = Solution()
    assert solution.longestCommonPrefix(input_strs) == expected_output
