class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """Do not return anything, modify board in-place instead."""

        def is_valid(num: str, row: int, col: int) -> bool:
            for i in range(9):
                if num in (board[row][i], board[i][col]):
                    return False

            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == num:
                        return False

            return True

        def solve() -> bool:
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        for num in map(str, range(1, 10)):
                            if is_valid(num, row, col):
                                board[row][col] = num
                                if solve():
                                    return True
                                board[row][col] = '.'
                        return False
            return True

        solve()
