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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack:
            node1, node2 = stack.pop()

            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False

            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))

        return True


def list_to_tree(lst: list[Optional[int]]) -> Optional[TreeNode]:
    if not lst:
        return None

    root = TreeNode(lst[0])
    stack = ([root])
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
print(solution.isSameTree(list_to_tree([1, 2, 3]), list_to_tree([1, 2, 3])))
print(solution.isSameTree(list_to_tree([1, 2]), list_to_tree([1, None, 2])))
print(solution.isSameTree(list_to_tree([1, 2, 1]), list_to_tree([1, 1, 2])))
