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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]) -> tuple[bool, int]:
            if not root:
                return (True, 0)

            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0]) and abs(left[1] - right[1]) <= 1

            return (balanced, 1 + max(left[1], right[1]))

        return dfs(root)[0]
