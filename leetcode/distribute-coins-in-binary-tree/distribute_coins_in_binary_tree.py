from typing import Optional, Tuple


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
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            if not node:
                return 0, 0

            left_moves, left_excess = dfs(node.left)
            right_moves, right_excess = dfs(node.right)

            total_moves = left_moves + right_moves
            total_excess = left_excess + right_excess + node.val - 1

            return total_moves + abs(total_excess), total_excess

        moves, _ = dfs(root)
        return moves


def build_tree(values: list[int]) -> Optional[TreeNode]:
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        node = queue.pop(0)
        if i < len(values):
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values):
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def main() -> None:
    values = [6, 2, 0, 0, 0, 0, 0, 0]
    root = build_tree(values)

    solution = Solution()

    moves = solution.distributeCoins(root)
    print(f"Number of moves required: {moves}")


if __name__ == "__main__":
    main()
