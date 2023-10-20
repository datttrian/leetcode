import pytest
from generate_parentheses.Solution import Solution  # Replace 'solution_module' with the actual module name

class TestSolution:
    @pytest.mark.parametrize("n, expected", [
        (1, ["()"]),
        (2, ["(())", "()()"]),
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"])
    ])
    def test_generateParenthesis(self, n, expected):
        solution = Solution()
        assert solution.generateParenthesis(n) == expected