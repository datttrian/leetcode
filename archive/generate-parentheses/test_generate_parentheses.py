from typing import List

import pytest
from generate_parentheses import Solution


@pytest.mark.parametrize(
    ('n', 'expected'),
    [
        (1, ['()']),
        (2, ['(())', '()()']),
        (3, ['((()))', '(()())', '(())()', '()(())', '()()()']),
    ],
)
def test_generateParenthesis(n: int, expected: List[str]):
    solution = Solution()
    assert solution.generateParenthesis(n) == expected
