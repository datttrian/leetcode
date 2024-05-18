from typing import Optional

import pytest
from distribute_coins_in_binary_tree import Solution, TreeNode


@pytest.mark.parametrize(
    "root, expected",
    [
        (TreeNode(3, TreeNode(0), TreeNode(0)), 2),
        (TreeNode(0, TreeNode(3), TreeNode(0)), 3),
        (TreeNode(1, TreeNode(0), TreeNode(2)), 2),
        (TreeNode(1, TreeNode(0, TreeNode(3)), TreeNode(0)), 4),
    ],
)
def test_distributeCoins(root: Optional[TreeNode], expected: int) -> None:
    solution = Solution()
    assert solution.distributeCoins(root) == expected
