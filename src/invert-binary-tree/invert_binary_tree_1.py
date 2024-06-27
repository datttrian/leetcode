from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Swap the left and right subtree
        root.left, root.right = root.right, root.left

        # Recursively invert the left and right subtree
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
