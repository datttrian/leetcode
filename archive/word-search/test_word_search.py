import pytest
from word_search import Solution


@pytest.mark.parametrize(
    ('board', 'word', 'expected'),
    [
        (
            [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],
            'ABCCED',
            True,
        ),
        (
            [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],
            'SEE',
            True,
        ),
        (
            [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],
            'ABCB',
            False,
        ),
        # Add more test cases as needed
    ],
)
def test_exist(board: list[list[str]], word: str, expected: bool):
    solution = Solution()
    result = solution.exist(board, word)
    assert result == expected
