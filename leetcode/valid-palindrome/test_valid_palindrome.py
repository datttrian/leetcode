import pytest
from valid_palindrome import Solution


@pytest.mark.parametrize(
    ["s", "expected"],
    [
        ["", True],  # Empty string is a palindrome.
        ["racecar", True],  # Basic case with a palindrome.
        ["hello", False],  # Basic case with a non-palindrome.
        [
            "A man, a plan, a canal, Panama",
            True,
        ],  # Case with spaces and punctuation.
        [
            "Was it a car or a cat I saw?",
            True,
        ],  # Case with spaces and punctuation.
        ["12321", True],  # Case with a numeric palindrome.
        ["no lemon, no melon", True],  # Case with spaces and punctuation.
        ["not a palindrome", False],  # Case with spaces and punctuation.
        ["Able , was I saw eLbA", True],  # Case with spaces and mixed case.
        ["@#*$#@!^", True],  # Case with special characters.
    ],
)
def test_is_palindrome(s: str, expected: bool) -> None:
    solution = Solution()
    result = solution.isPalindrome(s)
    assert result == expected
