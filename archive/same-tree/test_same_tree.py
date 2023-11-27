import pytest
from same_tree import Solution, TreeNode


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


# Define test cases
@pytest.mark.parametrize(
    "tree1, tree2, expected_result",
    [
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2, None], [1, None, 2], False),
        ([1, 2, 1], [1, 1, 2], False),
        # Add more test cases as needed
    ],
)
def test_isSameTree(
    tree1: list[int | None], tree2: list[int | None], expected_result: bool
):
    # Arrange
    solution = Solution()
    root1 = list_to_tree(tree1)
    root2 = list_to_tree(tree2)

    # Act
    result = solution.isSameTree(root1, root2)

    # Assert
    assert result == expected_result
