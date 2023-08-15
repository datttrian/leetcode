import pytest
from palindrome_number.Solution import Solution


class TestSolution:
    @pytest.mark.parametrize(
        "input_num, expected",
        [
            (121, True),
            (-121, False),
            (10, False),
            (0, True),
            (12321, True),
            (123456, False),
        ],
    )
    def test_isPalindrome(self, input_num, expected):
        solution = Solution()
        assert solution.isPalindrome(input_num) == expected
