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
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        if root.val == 0:
            return False
        if root.val == 1:
            return True

        left_eval = self.evaluateTree(root.left)
        right_eval = self.evaluateTree(root.right)

        if root.val == 2:
            return left_eval or right_eval

        if root.val == 3:
            return left_eval and right_eval

        return False
