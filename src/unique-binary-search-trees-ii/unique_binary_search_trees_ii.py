from typing import Union


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Union['TreeNode', None] = None,
        right: Union['TreeNode', None] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        if n == 0:
            return []

        def generate_trees_helper(
            start: int,
            end: int,
        ) -> list[TreeNode | None]:
            if start > end:
                return [None]

            result: list[TreeNode | None] = []
            for root_val in range(start, end + 1):
                left_trees = generate_trees_helper(start, root_val - 1)
                right_trees = generate_trees_helper(root_val + 1, end)

                for left_tree in left_trees:
                    for right_tree in right_trees:
                        root = TreeNode(root_val)
                        root.left = left_tree
                        root.right = right_tree
                        result.append(root)

            return result

        return generate_trees_helper(1, n)
