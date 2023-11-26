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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        :type root: TreeNode
        :rtype: bool
        """
        output: list[int] = []
        self.inorder(root, output)

        for i in range(1, len(output)):
            if output[i - 1] >= output[i]:
                return False

        return True

    # Time complexity of inorder traversal is O(n)
    # Fun fact: Inorder traversal leads to a sorted array if it is
    # a Valid Binary Search Tree.
    def inorder(self, root: Optional[TreeNode], output: list[int]) -> None:
        if root is None:
            return

        self.inorder(root.left, output)
        output.append(root.val)
        self.inorder(root.right, output)
