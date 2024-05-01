import pytest
from valid_palindrome import Solution


@pytest.mark.parametrize(
    ["s", "t", "expected_result"],
    [
        ["", "", True],
        ["a", "a", True],
        ["racecar", "racecar", True],
        ["hello", "world", False],
        ["abc", "cba", True],
        ["aab", "bba", False],
        ["abb", "bab", True],
        ["abcd", "dcba", True],
        [
            "abc",
            "defg",
            False,
        ],
    ],
)
def test_isPalindrome(s: str, t: str, expected_result: bool) -> None:
    solution = Solution()
    assert solution.isPalindrome(s, t) == expected_result
