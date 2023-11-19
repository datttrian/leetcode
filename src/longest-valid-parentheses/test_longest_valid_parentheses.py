import pytest
from longest_valid_parentheses import Solution


@pytest.mark.parametrize(
    ('s', 'expected_result'),
    [
        ('(()', 2),
        (')()())', 4),
        ('', 0),
        ('()(()', 2),
        ('()(()))', 6),
        ('((())', 4),
        (')(((((()())()()))()(()))(', 22),
        # ('))))()()()())', 4),
        ('(((((((', 0),
        (')()())()()(', 4),
    ],
)
def test_longestValidParentheses(s: str, expected_result: int):
    solution = Solution()
    result = solution.longestValidParentheses(s)
    assert result == expected_result
