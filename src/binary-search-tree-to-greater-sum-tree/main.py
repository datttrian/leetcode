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
    def bstToGst(self, root: TreeNode) -> TreeNode:
        stack: list[TreeNode] = []
        node = root
        total = 0

        while stack or node:
            while node:
                stack.append(node)
                node = node.right

            node = stack.pop()
            total += node.val
            node.val = total

            node = node.left

        return root
