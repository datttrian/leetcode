import pytest
from valid_parentheses.Solution import Solution  # Import the Solution class from your module

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("input_str, expected", [
        ("()", True),       # Simple valid case
        ("()[]{}", True),   # Multiple types of brackets
        ("(]", False),      # Incorrect closing bracket
        ("([)]", False),    # Incorrect nesting
        ("{[]}", True),     # Nested brackets
        ("", True),         # Empty string is valid
        ("[", False),       # Unbalanced opening bracket
        ("]", False),       # Unbalanced closing bracket
        ("(", False),       # Unbalanced opening bracket
        (")", False),       # Unbalanced closing bracket
    ])
    def test_is_valid(self, solution, input_str, expected):
        assert solution.isValid(input_str) == expected
