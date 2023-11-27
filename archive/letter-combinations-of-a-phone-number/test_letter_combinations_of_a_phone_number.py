from typing import List

import pytest
from letter_combinations_of_a_phone_number import Solution


@pytest.mark.parametrize(
    ('digits', 'expected'),
    [
        ('23', ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']),
        (
            '',
            [],
        ),  # Test case for an empty input, should return an empty list
        ('2', ['a', 'b', 'c']),
        ('7', ['p', 'q', 'r', 's']),
        ('9', ['w', 'x', 'y', 'z']),
        (
            '234',
            [
                'adg',
                'adh',
                'adi',
                'aeg',
                'aeh',
                'aei',
                'afg',
                'afh',
                'afi',
                'bdg',
                'bdh',
                'bdi',
                'beg',
                'beh',
                'bei',
                'bfg',
                'bfh',
                'bfi',
                'cdg',
                'cdh',
                'cdi',
                'ceg',
                'ceh',
                'cei',
                'cfg',
                'cfh',
                'cfi',
            ],
        ),  # Test case for multiple digits
    ],
)
def test_letterCombinations(digits: str, expected: List[str]):
    solution = Solution()
    assert solution.letterCombinations(digits) == expected
