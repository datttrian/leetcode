from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional['TreeNode'] = None,
        right: Optional['TreeNode'] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # Helper function to perform in-order traversal and identify misplaced nodes
        def inorder_traversal(node: Optional[TreeNode]) -> None:
            if node:
                inorder_traversal(node.left)

                # Check if current node is smaller than the previous node
                if prev[0] and node.val < prev[0].val:
                    # Identify the first misplaced node
                    if first[0] is None:
                        first[0] = prev[0]
                    # Identify the second misplaced node
                    second[0] = node

                prev[0] = node
                inorder_traversal(node.right)

        # Initialize variables to keep track of misplaced nodes
        first: list[Optional[TreeNode]] = [None]
        second: list[Optional[TreeNode]] = [None]
        prev: list[Optional[TreeNode]] = [None]

        # Perform in-order traversal to identify misplaced nodes
        inorder_traversal(root)

        # Swap the values of the misplaced nodes
        if first[0] and second[0]:
            first[0].val, second[0].val = second[0].val, first[0].val
