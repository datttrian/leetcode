import pytest
from happy_number import Solution


@pytest.mark.parametrize(
    ["n", "expected"],
    [
        [19, True],  # Basic case with a happy number.
        [2, False],  # Basic case with a non-happy number.
        [1, True],  # Minimal input case.
        [7, True],  # Another basic case with a happy number.
        [1111111, True],  # Case with a large happy number.
        [44, True],  # Case with a large happy number.
        [0, False],  # Edge case with zero.
    ],
)
def test_is_happy(n: int, expected: bool) -> None:
    solution = Solution()
    result = solution.isHappy(n)
    assert result == expected
