import pytest
from recursive import Solution


@pytest.mark.parametrize(
    ["n", "expected"],
    [
        [19, True],  # Basic case with a happy number.
        [2, False],  # Basic case with a non-happy number.
        [1, True],  # Minimal input case.
        [7, True],  # Another basic case with a happy number.
        [1111111, True],  # Case with a large non-happy number.
        [44, True],  # Case with a large happy number.
        [0, False],  # Edge case with zero.
    ],
)
def test_is_happy(n: int, expected: bool) -> None:
    """Test the isHappy function from the Solution class.

    Args:
    - n (int): Integer input.
    - expected (bool): Expected boolean output.

    Returns:
    - None
    """
    solution = Solution()
    result = solution.isHappy(n)
    assert result == expected
