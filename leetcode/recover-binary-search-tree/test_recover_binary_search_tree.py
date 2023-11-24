from typing import Optional
import pytest
from recover_binary_search_tree import Solution, TreeNode


@pytest.mark.parametrize(
    'root_values, expected_values',
    [
        (None, None),  # Test case with an empty tree
        ([5], [5]),  # Test case with a tree containing a single node
        (
            [1, 2, 3],
            [3, 2, 1],
        ),  # Test case with a sorted tree where two nodes are swapped
        (
            [3, 1, 2],
            [2, 1, 3],
        ),  # Test case with an unsorted tree where two nodes are swapped
        (
            [4, 7, 2, 1, 3, 6, 5],
            [6, 7, 2, 1, 3, 4, 5],
        ),  # Test case with a complex tree where multiple nodes are swapped
    ],
)
def test_recoverTree(
    solution: Solution,
    root_values: Optional[list[Optional[int]]],
    expected_values: Optional[list[Optional[int]]],
):
    root = create_tree(root_values)
    solution.recoverTree(root)
    assert tree_values(root) == expected_values


def create_tree(values: Optional[list[Optional[int]]]) -> Optional[TreeNode]:
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    for i, node in enumerate(nodes):
        if node:
            left_child_idx = 2 * i + 1
            right_child_idx = 2 * i + 2
            if left_child_idx < len(nodes):
                node.left = nodes[left_child_idx]
            if right_child_idx < len(nodes):
                node.right = nodes[right_child_idx]
    return nodes[0]


def tree_values(root: Optional[TreeNode]) -> list[Optional[int]]:
    values: list[Optional[int]] = []
    if not root:
        return values
    stack: list[Optional[TreeNode]] = [root]
    while stack:
        node: Optional[TreeNode] = stack.pop()
        if node:
            values.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        else:
            values.append(None)
    return values
