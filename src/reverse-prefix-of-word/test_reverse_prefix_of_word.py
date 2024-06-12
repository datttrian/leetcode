import pytest
from reverse_prefix_of_word import Solution


@pytest.mark.parametrize(
    ["word", "ch", "expected_result"],
    [
        ["abcdef", "c", "cbadef"],
        ["abcd", "e", "abcd"],
        ["", "a", ""],
        ["abcd", "d", "dcba"],
        ["abcdef", "z", "abcdef"],
    ],
)
def test_reversePrefix(word: str, ch: str, expected_result: str) -> None:
    solution = Solution()
    assert solution.reversePrefix(word, ch) == expected_result
