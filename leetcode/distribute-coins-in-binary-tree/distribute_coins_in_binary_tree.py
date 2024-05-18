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


def main() -> None:
    #        3
    #       / \
    #      0   0
    root = TreeNode(0)
    root.left = TreeNode(3)
    root.right = TreeNode(0)

    # Create a Solution object
    solution = Solution()

    # Call the distributeCoins method and print the result
    moves = solution.distributeCoins(root)
    print(f"Number of moves required: {moves}")


if __name__ == "__main__":
    main()
