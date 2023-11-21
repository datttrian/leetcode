from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(i: int) -> None:
            if i == n:
                res.append(list(board))
            for j in range(n):
                if (
                    j not in cols
                    and j - i not in diag
                    and j + i not in off_diag
                ):
                    cols.add(j)
                    diag.add(j - i)
                    off_diag.add(j + i)
                    board.append('.' * (j) + 'Q' + '.' * (n - j - 1))
                    backtrack(i + 1)
                    board.pop()
                    off_diag.remove(j + i)
                    diag.remove(j - i)
                    cols.remove(j)

        res: List[List[str]] = []
        board: List[str] = []  # Changed the type to List[str]
        cols: set[int] = set()  # Assuming column indices are integers
        diag: set[int] = set()
        off_diag: set[int] = set()
        backtrack(0)
        return res
