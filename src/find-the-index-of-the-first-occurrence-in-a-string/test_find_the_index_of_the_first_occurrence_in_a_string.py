import pytest
from find_the_index_of_the_first_occurrence_in_a_string import Solution


class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize(
        "haystack, needle, expected",
        [
            ("hello", "ll", 2),
            ("aaaaa", "bba", -1),
            ("", "", 0),
            ("abcde", "e", 4),
            ("abcde", "z", -1),
        ],
    )
    def test_strStr(self, solution, haystack, needle, expected):
        result = solution.strStr(haystack, needle)
        assert result == expected
