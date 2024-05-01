import pytest
from h_index import Solution


@pytest.mark.parametrize(
    ["citations", "expected_h_index"],
    [
        [[3, 0, 6, 1, 5], 3],
        [[1, 2, 3, 4, 5], 3],
        [[0, 0, 0, 0, 0], 0],
        [[4, 4, 4, 4, 5], 4],
        [[0, 1, 3, 5, 6], 3],
    ],
)
def test_hIndex(citations: list[int], expected_h_index: int) -> None:
    solution = Solution()
    assert solution.hIndex(citations) == expected_h_index
