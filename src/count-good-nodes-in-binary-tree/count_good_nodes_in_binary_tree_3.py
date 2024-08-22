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
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        queue = deque([(root, root.val)])

        while queue:
            node, max_val = queue.popleft()

            if node.val and max_val and node.val >= max_val:
                count += 1

            if max_val and node.val:
                max_val = max(max_val, node.val)

            if node.left:
                queue.append((node.left, max_val))
            if node.right:
                queue.append((node.right, max_val))

        return count
