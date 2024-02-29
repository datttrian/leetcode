class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def dfs(i: int, j: int, k: int):
            if (
                not (0 <= i < len(board))
                or not (0 <= j < len(board[0]))
                or board[i][j] != word[k]
            ):
                return False

            if k == len(word) - 1:
                return True

            tmp, board[i][j] = board[i][j], '/'
            if (
                dfs(i + 1, j, k + 1)
                or dfs(i - 1, j, k + 1)
                or dfs(i, j + 1, k + 1)
                or dfs(i, j - 1, k + 1)
            ):
                return True

            board[i][j] = tmp
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True

        return False
