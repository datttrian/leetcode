import pytest
from maximize_happiness_of_selected_children import Solution


@pytest.mark.parametrize(
    "happiness,k,expected",
    [
        ([1, 2, 3], 1, 3),
    ],
)
def test_maximumHappinessSum(happiness: list[int], k: int, expected: int) -> None:
    solution = Solution()
    assert solution.maximumHappinessSum(happiness, k) == expected
