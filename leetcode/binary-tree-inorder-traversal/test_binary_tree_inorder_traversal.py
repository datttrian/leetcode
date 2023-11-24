from typing import Optional
import pytest
from binary_tree_inorder_traversal import Solution, TreeNode


# Helper function to create a binary tree from a list
def list_to_tree(lst: list[Optional[int]]) -> TreeNode | None:
    if not lst:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in lst]
    for i, node in enumerate(nodes):
        if node:
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            if left_child < len(nodes):
                node.left = nodes[left_child]
            if right_child < len(nodes):
                node.right = nodes[right_child]

    return nodes[0]


@pytest.mark.parametrize(
    ('tree_values', 'expected_result'),
    [
        # ([1, None, 2, 3], [1, 3, 2]),
        # ([], []),
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, None, 2], [1, 2]),
        # ([1, None, 2, None, 3], [1, 3, 2]),
        # Add more test cases as needed
    ],
)
def test_inorderTraversal(
    tree_values: list[Optional[int]],
    expected_result: list[int],
):
    solution = Solution()
    tree_root = list_to_tree(tree_values)

    result = solution.inorderTraversal(tree_root)

    assert result == expected_result
