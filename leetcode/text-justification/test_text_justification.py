import pytest
from text_justification import Solution


@pytest.mark.parametrize(
    ('words', 'maxWidth', 'expected'),
    [
        (
            ['This', 'is', 'an', 'example', 'of', 'text', 'justification.'],
            16,
            ['This    is    an', 'example  of text', 'justification.  '],
        ),
        (
            ['What', 'must', 'be', 'acknowledgment', 'shall', 'be'],
            16,
            ['What   must   be', 'acknowledgment  ', 'shall be        '],
        ),
        (
            [
                'Science',
                'is',
                'what',
                'we',
                'understand',
                'well',
                'enough',
                'to',
                'explain',
                'to',
                'a',
                'computer.',
                'Art',
                'is',
                'everything',
                'else',
                'we',
                'do',
            ],
            20,
            [
                'Science  is  what we',
                'understand      well',
                'enough to explain to',
                'a  computer.  Art is',
                'everything  else  we',
                'do                  ',
            ],
        ),
    ],
)
def test_fullJustify(words: list[str], maxWidth: int, expected: list[str]):
    solution = Solution()
    result = solution.fullJustify(words, maxWidth)
    assert result == expected
