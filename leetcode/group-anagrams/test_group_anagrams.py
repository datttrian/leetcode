from typing import List

import pytest
from group_anagrams import Solution


@pytest.mark.parametrize(
    ('strs', 'expected'),
    [
        (
            ['eat', 'tea', 'tan', 'ate', 'nat', 'bat'],
            [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']],
        ),
        (['listen', 'silent', 'enlist'], [['listen', 'silent', 'enlist']]),
        (['a'], [['a']]),
        ([''], [['']]),
        ([], []),
        (['abc', 'def', 'xyz'], [['abc'], ['def'], ['xyz']]),
        (
            ['hello', 'world', 'dlrow', 'olleh'],
            [['hello', 'olleh'], ['world', 'dlrow']],
        ),
    ],
)
def test_groupAnagrams(strs: List[str], expected: List[List[str]]):
    solution = Solution()
    result = solution.groupAnagrams(strs)
    assert result == expected
