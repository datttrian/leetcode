import pytest
from valid_parentheses import \
    Solution  # Import the Solution class from your module


@pytest.mark.parametrize(
    ('input_str', 'expected'),
    [
        ('()', True),  # Simple valid case
        ('()[]{}', True),  # Multiple types of brackets
        ('(]', False),  # Incorrect closing bracket
        ('([)]', False),  # Incorrect nesting
        ('{[]}', True),  # Nested brackets
        ('', True),  # Empty string is valid
        ('[', False),  # Unbalanced opening bracket
        (']', False),  # Unbalanced closing bracket
        ('(', False),  # Unbalanced opening bracket
        (')', False),  # Unbalanced closing bracket
    ],
)
def test_is_valid(input_str: str, expected: bool):
    solution = Solution()
    assert solution.isValid(input_str) == expected
