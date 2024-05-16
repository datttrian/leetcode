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
            raise ValueError("Root cannot be None")

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

        raise ValueError("Invalid node value")


if __name__ == "__main__":
    solution = Solution()
    result = solution.evaluateTree(TreeNode(3, TreeNode(1), TreeNode(0)))
    print(result)
