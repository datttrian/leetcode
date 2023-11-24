import pytest
from substring_with_concatenation_of_all_words import Solution
from typing import List


@pytest.mark.parametrize(
    ('s', 'words', 'expected_result'),
    [
        ('barfoothefoobarman', ['foo', 'bar'], [0, 9]),
        # ('wordgoodgoodgoodbestword', ['word', 'good', 'best', 'word'], [8]),
        ('barfoofoobarthefoobarman', ['bar', 'foo', 'the'], [6, 9, 12]),
        ('aaa', ['a', 'a'], [0, 1]),
        # ('abababab', ['ab', 'ba'], [0, 2, 4]),
        # ('aaaa', ['a', 'a', 'a'], [0, 1, 2]),
        ('', ['foo', 'bar'], []),
        ('barfoobar', [], []),
    ],
)
def test_findSubstring(s: str, words: List[str], expected_result: List[int]):
    solution = Solution()
    result = solution.findSubstring(s, words)
    assert result == expected_result
