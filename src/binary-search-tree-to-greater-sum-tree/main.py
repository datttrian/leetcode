from typing import Optional, Union


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
    def bstToGst(self, root: TreeNode) -> TreeNode:
        stack: list[TreeNode] = []
        node: Optional[TreeNode] = root
        total = 0

        while stack or node:

            while node:
                stack.append(node)
                node = node.right

            node = stack.pop()
            total += node.val
            node.val = total
            node = node.left

        return root


def list_to_tree(lst: list[int]) -> Optional[TreeNode]:
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while i < len(lst):
        current = queue.pop(0)
        if lst[i] is not None:  # type: ignore
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        i += 1
        if i < len(lst) and lst[i] is not None:  # type: ignore
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1
    return root


def tree_to_list(root: Optional[TreeNode]) -> list[Union[int, None]]:
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)  # type: ignore
            queue.append(node.left)  # type: ignore
            queue.append(node.right)  # type: ignore
        else:
            result.append(None)  # type: ignore
    # Trim the trailing None values
    while result and result[-1] is None:
        result.pop()
    return result  # type: ignore


# Input tree
input_list = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
input_tree = list_to_tree(input_list)  # type: ignore

solution = Solution()
# Transform the BST
new_root = solution.bstToGst(input_tree)  # type: ignore

# Output the transformed tree as a list
output_list = tree_to_list(new_root)
print(output_list)
