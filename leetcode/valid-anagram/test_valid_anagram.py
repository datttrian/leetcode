import pytest
from valid_anagram import Solution


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        ("", "", True),
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("listen", "silent", True),
        ("abc", "def", False),
        ("listen", "silent", True),
        ("evil", "vile", True),
        ("racecar", "racecar", True),
    ],
)
def test_isAnagram(s: str, t: str, expected: bool) -> None:
    solution = Solution()
    assert solution.isAnagram(s, t) == expected
