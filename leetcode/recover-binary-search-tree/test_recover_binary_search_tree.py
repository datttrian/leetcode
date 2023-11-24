from typing import Optional, List
from recover_binary_search_tree import Solution, TreeNode
import pytest


def inorder_traversal(root: Optional['TreeNode']) -> List[int]:
    """Helper function to perform in-order traversal and return values in a list."""
    result: List[int] = []
    stack: List[Optional['TreeNode']] = []
    current: TreeNode | None = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        if current:
            result.append(current.val)
            current = current.right

    return result


@pytest.mark.parametrize(
    'tree: Optional[TreeNode | None], expected: List[int]',
    [
        (TreeNode(1, TreeNode(3), TreeNode(2)), [1, 2, 3]),  # Correct BST
        (
            TreeNode(3, TreeNode(1), TreeNode(4, TreeNode(2))),
            [1, 2, 3, 4],
        ),  # Misplaced nodes: 3, 1
        (TreeNode(2, TreeNode(3, TreeNode(1))), [1, 2, 3]),  # Correct BST
        (
            TreeNode(3, TreeNode(1), TreeNode(2, TreeNode(4))),
            [1, 2, 3, 4],
        ),  # Misplaced nodes: 2, 1
        (None, []),  # Empty tree
        # Add more test cases as needed
    ],
)
def test_recoverTree(tree: Optional[TreeNode], expected: List[int]):
    solution = Solution()
    solution.recoverTree(tree)
    assert inorder_traversal(tree) == expected
