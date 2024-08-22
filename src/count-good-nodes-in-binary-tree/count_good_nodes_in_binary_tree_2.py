from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: Optional[int] = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        stack = [(root, float("-inf"))]

        while stack:
            node, largest = stack.pop()

            if node.val and largest <= node.val:
                good += 1

            if node.val:
                largest = max(largest, node.val)

            if node.right:
                stack.append((node.right, largest))

            if node.left:
                stack.append((node.left, largest))

        return good
