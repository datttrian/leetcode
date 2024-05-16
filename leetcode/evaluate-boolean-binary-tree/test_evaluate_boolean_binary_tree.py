from typing import Optional
import pytest
from evaluate_boolean_binary_tree import TreeNode, Solution


@pytest.mark.parametrize(
    "root, expected",
    [
        (
            TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0), TreeNode(1))),
            True,
        ),  # Example 1
        (TreeNode(0), False),  # Example 2
        (
            TreeNode(3, TreeNode(1), TreeNode(1)),
            True,
        ),  # AND operation with both True
        (
            TreeNode(3, TreeNode(1), TreeNode(0)),
            False,
        ),  # AND operation with one False
        (
            TreeNode(2, TreeNode(0), TreeNode(1)),
            True,
        ),  # OR operation with one True
        (
            TreeNode(2, TreeNode(0), TreeNode(0)),
            False,
        ),  # OR operation with both False
        (
            TreeNode(
                2,
                TreeNode(3, TreeNode(1), TreeNode(1)),
                TreeNode(3, TreeNode(0), TreeNode(1)),
            ),
            True,
        ),  # Mixed operations
    ],
)
def test_evaluateTree(root: Optional[TreeNode], expected: bool) -> None:
    solution = Solution()
    assert solution.evaluateTree(root) == expected


if __name__ == "__main__":
    pytest.main()
