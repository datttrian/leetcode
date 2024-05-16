from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            raise ValueError("Root cannot be None")

        # If the node is a leaf, return its boolean value
        if root.val == 0:
            return False
        if root.val == 1:
            return True

        # Recursively evaluate the left and right children
        left_eval = self.evaluateTree(root.left)
        right_eval = self.evaluateTree(root.right)

        # If the node is an OR node
        if root.val == 2:
            return left_eval or right_eval

        # If the node is an AND node
        if root.val == 3:
            return left_eval and right_eval

        # This point should never be reached if the input is valid
        raise ValueError("Invalid node value: must be 0, 1, 2, or 3")
