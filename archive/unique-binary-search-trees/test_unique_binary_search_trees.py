import pytest
from unique_binary_search_trees import Solution


@pytest.mark.parametrize(
    'n, expected',
    [
        # (0, 1),  # Empty tree
        (1, 1),  # Single-node tree
        (2, 2),  # Two-node trees: 1 root, 1 left child or 1 right child
        (
            3,
            5,
        ),  # Three-node trees: 1 root, 2 left children or 1 root, 1 left child, 1 right child, and so on
        (4, 14),  # Four-node trees
        # Add more test cases as needed
    ],
)
def test_numTrees(n: int, expected: int):
    solution = Solution()
    assert solution.numTrees(n) == expected
