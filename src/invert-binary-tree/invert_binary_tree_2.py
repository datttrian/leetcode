from collections import deque
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

        stack = deque([root])

        while stack:
            current = stack.pop()

            # Swap the left and right subtree
            current.left, current.right = current.right, current.left

            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

        return root

