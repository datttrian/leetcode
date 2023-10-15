import pytest
from integer_to_roman.Solution import Solution  # Assuming your solution is in a module named solution_module

class TestSolution:
    @pytest.mark.parametrize("num, expected_roman", [
        (1, "I"),
        (4, "IV"),
        (9, "IX"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
        # Add more test cases as needed
    ])
    def test_intToRoman(self, num, expected_roman):
        solution = Solution()
        result = solution.intToRoman(num)
        assert result == expected_roman
