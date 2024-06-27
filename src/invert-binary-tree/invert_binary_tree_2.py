from collections import deque
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        stack = deque([root])

        while stack:
            current = stack.pop()

            # Swap the left and right subtree
            current.left, current.right = current.right, current.left

            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

        return root


def list_to_tree(nodes: list[int]) -> Optional[TreeNode]:
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1

    while i < len(nodes):
        current = queue.popleft()

        current.left = TreeNode(nodes[i])
        queue.append(current.left)
        i += 1

        if i < len(nodes):
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1

    return root


def tree_to_list(root: Optional[TreeNode]) -> list[Optional[int]]:
    if not root:
        return []

    result: list[Optional[int]] = []
    queue: deque[Optional[TreeNode]] = deque([root])

    while queue:
        current = queue.popleft()
        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)

    # Remove trailing None values that are not needed for the representation
    while result and result[-1] is None:
        result.pop()

    return result


solution = Solution()
print(tree_to_list(solution.invertTree(list_to_tree([4, 2, 7, 1, 3, 6, 9]))))
