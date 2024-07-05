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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack: list[tuple[Optional[TreeNode], bool]] = [(root, False)]
        depth: dict[Optional[TreeNode], int] = {}
        diameter = 0

        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    left_depth = depth.get(node.left, 0)
                    right_depth = depth.get(node.right, 0)
                    depth[node] = max(left_depth, right_depth) + 1
                    diameter = max(diameter, left_depth + right_depth)
                else:
                    stack.append((node, True))
                    stack.append((node.left, False))
                    stack.append((node.right, False))

        return diameter
