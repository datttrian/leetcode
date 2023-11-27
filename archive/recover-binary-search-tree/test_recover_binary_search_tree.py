from typing import Optional

import pytest
from recover_binary_search_tree import Solution, TreeNode


# Define a helper function to convert a list to a binary tree
def list_to_tree(lst: list[int | None]) -> TreeNode | None:
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


# Define a helper function to convert a binary tree to a list
def tree_to_list(root: TreeNode | None) -> list[Optional[int]]:
    if not root:
        return []

    result: list[int | None] = []
    queue: list[TreeNode | None] = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    return result


# Define test cases
@pytest.mark.parametrize(
    "input_tree, expected_output_tree",
    [
        ([1, 3, None, None, 2], [3, 1, None, None, 2]),
        ([3, 1, 4, None, None, 2], [2, 1, 4, None, None, 3]),
        # ([10, 5, 15, None, None, 7, 20], [10, 7, 15, None, None, 5, 20]),
        # Add more test cases as needed
    ],
)
def test_recoverTree(
    input_tree: list[int | None], expected_output_tree: list[int | None]
):
    # Arrange
    solution = Solution()
    root = list_to_tree(input_tree)
    expected_output = list_to_tree(expected_output_tree)

    # Act
    solution.recoverTree(root)

    # Assert
    assert tree_to_list(root) == tree_to_list(expected_output)
