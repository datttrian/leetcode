import pytest
from find_the_index_of_the_first_occurrence_in_a_string import Solution


@pytest.mark.parametrize(
    ('haystack', 'needle', 'expected_result'),
    [
        ('', '', 0),
        ('hello', '', 0),
        ('hello', 'll', 2),
        ('aaaaa', 'bba', -1),
        ('abcdef', 'ef', 4),
        ('abc', 'abcd', -1),
        ('abc', 'abc', 0),
    ],
)
def test_strStr(haystack: str, needle: str, expected_result: int):
    solution = Solution()
    result = solution.strStr(haystack, needle)
    assert result == expected_result
