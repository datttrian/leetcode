import pytest
from divide_two_integers.Solution import Solution


class TestSolution:
    @pytest.mark.parametrize(
        "dividend, divisor, expected",
        [
            # Normal positive division
            (10, 3, 3),  # 10 / 3 = 3 remainder 1
            # Normal negative division
            (7, -3, -2),  # 7 / (-3) = -2 remainder 1
            # Division by -1
            (-2147483648, -1, 2147483647),  # -2147483648 / (-1) = 2147483647
            # Division by 0 (should return 0)
            (0, 1, 0),  # 0 / 1 = 0
            # Division of a number by itself (should return 1)
            (1, 1, 1),  # 1 / 1 = 1
            # Division by 1 (should return the dividend)
            (123456789, 1, 123456789),
            # Division by a large divisor
            (10, 10000, 0),  # 10 / 10000 = 0
            # Division by 0 (should return 0)
            # (10000, 0, 0),  # Division by zero
            # Dividend and divisor both 0 (should return 0)
            # (0, 0, 0),
        ],
    )
    def test_divide(self, dividend, divisor, expected):
        solution = Solution()
        result = solution.divide(dividend, divisor)
        assert result == expected
