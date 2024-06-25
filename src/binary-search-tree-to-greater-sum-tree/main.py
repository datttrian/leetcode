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


root = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]


def list_to_tree(lst):  # type: ignore
    if not lst:
        return None
    root = TreeNode(lst[0])  # type: ignore
    queue = [root]
    i = 1
    while i < len(lst):  # type: ignore
        current = queue.pop(0)
        if lst[i] is not None:
            current.left = TreeNode(lst[i])  # type: ignore
            queue.append(current.left)
        i += 1
        if i < len(lst) and lst[i] is not None:  # type: ignore
            current.right = TreeNode(lst[i])  # type: ignore
            queue.append(current.right)
        i += 1
    return root


root_tree = list_to_tree(root)
print(root_tree)


stack = []
print(stack)  # type: ignore
print(root_tree)
stack.append(root_tree)  # type: ignore
print(stack)  # type: ignore
print(root_tree.left)  # type: ignore


node = root_tree.left  # type: ignore
print(node.val)  # type: ignore


def bstToGst(root: TreeNode) -> TreeNode:
    stack = []

    while stack or root:
        while root:
            stack.append(root)  # type: ignore
            root = root.left  # type: ignore

    return TreeNode(0)  # Return the modified root
