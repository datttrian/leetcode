from typing import Optional
import pytest
from evaluate_boolean_binary_tree import Solution, TreeNode


@pytest.mark.parametrize(
    "root, expected",
    [
        (
            TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0), TreeNode(1))),
            True,
        ),
        (TreeNode(0), False),
        (
            TreeNode(3, TreeNode(1), TreeNode(1)),
            True,
        ),
        (
            TreeNode(3, TreeNode(1), TreeNode(0)),
            False,
        ),
        (
            TreeNode(2, TreeNode(0), TreeNode(1)),
            True,
        ),
        (
            TreeNode(2, TreeNode(0), TreeNode(0)),
            False,
        ),
        (
            TreeNode(
                2,
                TreeNode(3, TreeNode(1), TreeNode(1)),
                TreeNode(3, TreeNode(0), TreeNode(1)),
            ),
            True,
        ),
    ],
)
def test_evaluateTree(root: Optional[TreeNode], expected: bool) -> None:
    solution = Solution()
    assert solution.evaluateTree(root) == expected
