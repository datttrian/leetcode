from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(board: List[List[str]], row: int, col: int) -> bool:
            # Check if there is a queen in the same column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            # Check upper left diagonal
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == 'Q':
                    return False

            # Check upper right diagonal
            for i, j in zip(range(row, -1, -1), range(col, n)):
                if board[i][j] == 'Q':
                    return False

            return True

        def create_board() -> List[List[str]]:
            return [['.' for _ in range(n)] for _ in range(n)]

        def format_solution(board: List[List[str]]) -> List[str]:
            return [''.join(row) for row in board]

        def solve(
            board: List[List[str]],
            row: int,
            solutions: List[List[str]],
        ) -> None:
            if row == n:
                solutions.append(format_solution(board))
                return

            for col in range(n):
                if is_safe(board, row, col):
                    board[row][col] = 'Q'
                    solve(board, row + 1, solutions)
                    board[row][col] = '.'

        # Initialize the chessboard
        chessboard = create_board()
        solutions: List[List[str]] = []
        solve(chessboard, 0, solutions)
        return solutions
