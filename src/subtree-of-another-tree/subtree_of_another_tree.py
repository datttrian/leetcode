from typing import Optional


# Definition for a binary tree node.
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return (
            False
            if not root
            else self.isSameTree(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return (
            p == q
            if not p or not q
            else (
                p.val == q.val
                and self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right)
            )
        )


def list_to_tree(lst: list[Optional[int]]) -> Optional[TreeNode]:
    if not lst:
        return None

    root = TreeNode(lst[0])
    stack = [root]
    i = 1

    while i < len(lst):
        current = stack.pop()

        current.left = TreeNode(lst[i])
        stack.append(current.left)
        i += 1

        if i < len(lst):
            current.right = TreeNode(lst[i])
            stack.append(current.right)
        i += 1

    return root


solution = Solution()
print(solution.isSubtree(list_to_tree(
    [3, 4, 5, 1, 2]), list_to_tree([4, 1, 2])))
print(solution.isSubtree(list_to_tree(
    [3, 4, 5, 1, 2, None, None, None, None, 0]), list_to_tree([4, 1, 2])))
