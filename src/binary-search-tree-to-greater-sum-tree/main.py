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
print(queue)

temp = queue.pop(0)
print(temp)
print(queue)


print(temp.left)
print(temp.right)
