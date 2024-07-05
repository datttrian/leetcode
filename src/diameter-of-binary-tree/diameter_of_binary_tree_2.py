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
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0

        def depth(node: Optional["TreeNode"]) -> int:
            if not node:
                return 0
            left_depth = depth(node.left)
            right_depth = depth(node.right)

            # The path through this node
            self.diameter = max(self.diameter, left_depth + right_depth)

            # Return the depth of the tree rooted at this node
            return max(left_depth, right_depth) + 1

        depth(root)
        return self.diameter
