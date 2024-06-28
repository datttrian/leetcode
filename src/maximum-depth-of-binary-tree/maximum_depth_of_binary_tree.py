from collections import deque
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


def list_to_tree(lst: list[Optional[int]]) -> Optional[TreeNode]:
    if not lst:
        return None

    root = TreeNode(lst[0]) if lst[0] is not None else None
    queue = deque([root])
    i = 1

    while i < len(lst):
        current = queue.popleft()

        if current:
            if i < len(lst) and lst[i] is not None:
                current.left = TreeNode(lst[i])
                queue.append(current.left)
            i += 1

            if i < len(lst) and lst[i] is not None:
                current.right = TreeNode(lst[i])
                queue.append(current.right)
            i += 1

    return root


solution = Solution()
print(solution.maxDepth(list_to_tree([3, 9, 20, None, None, 15, 7])))
