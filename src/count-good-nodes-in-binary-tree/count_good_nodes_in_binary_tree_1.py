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
        def dfs(node: Optional[TreeNode], max_val: int) -> int:
            if node is None:
                return 0

            good = 0
            if node.val:
                good = 1 if node.val >= max_val else 0
                max_val = max(max_val, node.val)

            good += dfs(node.left, max_val)
            good += dfs(node.right, max_val)

            return good

        return dfs(root, root.val if root.val else -10 ^ 4)
