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
        def dfs(node: Optional[TreeNode], maxVal: int) -> int:
            if node is None:
                return 0

            count = 0
            if node.val:
                count = 1 if node.val >= maxVal else 0
                maxVal = max(maxVal, node.val)

            count += dfs(node.left, maxVal)
            count += dfs(node.right, maxVal)

            return count

        return dfs(root, root.val if root.val else -10 ^ 4)
