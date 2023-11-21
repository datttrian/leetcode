from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_valid(board: List[int], row: int, col: int) -> bool:
            for i in range(row):
                if (
                    board[i] == col
                    or board[i] - i == col - row
                    or board[i] + i == col + row
                ):
                    return False
            return True

        def place_queens(row: int) -> None:
            if row == n:
                result.append(
                    [
                        ''.join(
                            [
                                'Q' if col == board[row] else '.'
                                for col in range(n)
                            ],
                        )
                        for row in range(n)
                    ],
                )
                return

            for col in range(n):
                if is_valid(board, row, col):
                    board[row] = col
                    place_queens(row + 1)
                    board[row] = -1

        result: List[List[str]] = []
        board: List[int] = [
            -1,
        ] * n
        place_queens(0)
        return result
