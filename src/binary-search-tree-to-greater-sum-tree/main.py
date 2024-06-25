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

queue = [TreeNode(root[1])]  # type: ignore
print(queue)
queue.append(TreeNode(root[2]))  # type: ignore
queue.append(TreeNode(root[3]))  # type: ignore
queue.append(TreeNode(root[4]))  # type: ignore
queue.append(TreeNode(root[5]))  # type: ignore
print(queue)

current = queue.pop(2)

print(current)
print(current.right)

current.right = TreeNode(root[1])  # type: ignore
print(current)
print(current.right)


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
        
    return root


print(list_to_tree(root))
print(TreeNode(root[0]))  # type: ignore
