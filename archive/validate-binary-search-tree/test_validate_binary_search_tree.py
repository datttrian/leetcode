import pytest
from validate_binary_search_tree import Solution, TreeNode


@pytest.mark.parametrize(
    'root, expected',
    [
        (TreeNode(2, TreeNode(1), TreeNode(3)), True),  # Valid BST
        (
            TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6))),
            False,
        ),  # Invalid BST
        (TreeNode(1, TreeNode(1)), False),  # Invalid BST with duplicate values
        (None, True),  # Empty tree is considered a valid BST
        # Add more test cases as needed
    ],
)
def test_isValidBST(root: TreeNode | None, expected: bool):
    solution = Solution()
    assert solution.isValidBST(root) == expected
