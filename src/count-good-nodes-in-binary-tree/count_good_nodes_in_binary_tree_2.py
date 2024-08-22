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
        count = 0
        stack = [(root, root.val)]

        while stack:
            node, max_val = stack.pop()

            if node.val and max_val and max_val <= node.val:
                count += 1

            if node.val and max_val:
                max_val = max(max_val, node.val)

            if node.right:
                stack.append((node.right, max_val))

            if node.left:
                stack.append((node.left, max_val))

        return count
