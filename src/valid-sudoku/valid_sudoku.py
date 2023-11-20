from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check each row
        for i in range(9):
            row_set: set[str] = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in row_set:
                        return False
                    row_set.add(board[i][j])

        # Check each column
        for j in range(9):
            col_set: set[str] = set()
            for i in range(9):
                if board[i][j] != '.':
                    if board[i][j] in col_set:
                        return False
                    col_set.add(board[i][j])

        # Check each 3x3 sub-box
        for box in range(9):
            box_set: set[str] = set()
            for i in range(box // 3 * 3, box // 3 * 3 + 3):
                for j in range(box % 3 * 3, box % 3 * 3 + 3):
                    if board[i][j] != '.':
                        if board[i][j] in box_set:
                            return False
                        box_set.add(board[i][j])

        return True
