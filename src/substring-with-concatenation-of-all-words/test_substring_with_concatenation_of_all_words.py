import pytest
from substring_with_concatenation_of_all_words.Solution import Solution


class TestSolution:
    @pytest.fixture
    def solution_instance(self):
        return Solution()

    @pytest.mark.parametrize(
        "s, words, expected",
        [
            # Test case with a single word in s
            ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], []),
            # Test case with multiple occurrences of the same word
            ("foofoofoo", ["foo"], [0, 3, 6]),
            # Test case with multiple words in s
            ("barfoothefoobarman", ["foo", "bar"], [0, 9]),
            # Test case with words not in s
            ("hello", ["world"], []),
            # Test case with words appearing in reverse order
            ("barfoothemanfoo", ["foo", "bar"], [0]),
            # Test case with words as substrings of other words
            ("wordgoodgoodgoodbest", ["word", "good", "best"], []),
        ],
    )
    def test_findSubstring(self, solution_instance, s, words, expected):
        result = solution_instance.findSubstring(s, words)
        assert result == expected, f"Expected {expected}, but got {result}"
