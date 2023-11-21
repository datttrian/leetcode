from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_safe(board: List[List[int]], row: int, col: int) -> bool:
            # Check if there is a queen in the same column
            for i in range(row):
                if board[i][col] == 1:
                    return False

            # Check upper left diagonal
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == 1:
                    return False

            # Check upper right diagonal
            for i, j in zip(range(row, -1, -1), range(col, n)):
                if board[i][j] == 1:
                    return False

            return True

        def solve(board: List[List[int]], row: int) -> int:
            if row == n:
                return 1

            count = 0
            for col in range(n):
                if is_safe(board, row, col):
                    board[row][col] = 1
                    count += solve(board, row + 1)
                    board[row][col] = 0

            return count

        # Initialize the chessboard
        chessboard = [[0] * n for _ in range(n)]
        return solve(chessboard, 0)
