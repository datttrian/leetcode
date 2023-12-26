import pytest
from palindrome_number import Solution


@pytest.mark.parametrize(
    ["input_num", "expected"],
    [
        [121, True],
        [-121, False],
        [10, False],
        [0, True],
        [12321, True],
        [123456, False],
    ],
)
def test_is_palindrome(input_num: int, expected: bool) -> None:
    """Test the isPalindrome function from the Solution class.

    Args:
    - x (int): Input number.

    Returns:
    - None
    """
    solution = Solution()
    assert solution.isPalindrome(input_num) == expected
