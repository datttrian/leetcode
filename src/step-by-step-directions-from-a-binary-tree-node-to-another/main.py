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


def list_to_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        current = queue.pop(0)
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    return root


def tree_to_list(root: Optional[TreeNode]) -> list[Optional[int]]:

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

    while result and result[-1] is None:
        result.pop()

    return result


startValue = 3
destValue = 6
t = list_to_tree([5, 1, 2, 3, None, 6, 4])


def find_path(node, value, path):
    if not node:
        return False
    if node.val == value:
        return True

    path.append('L')
    if find_path(node.left, value, path):
        return True
    path.pop()

    path.append('R')
    if find_path(node.right, value, path):
        return True
    path.pop()

    return False


print(find_path(t, startValue, []))
print(find_path(t, destValue, []))
