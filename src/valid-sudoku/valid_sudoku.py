from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_line(line: List[str]) -> bool:
            line_set: set[str] = set()
            for cell in line:
                if cell != '.':
                    if cell in line_set:
                        return False
                    line_set.add(cell)
            return True

        def is_valid_board_lines(board: List[List[str]]) -> bool:
            for i in range(9):
                if not is_valid_line(board[i]) or not is_valid_line(
                    [board[j][i] for j in range(9)],
                ):
                    return False
            return True

        def is_valid_box(
            board: List[List[str]],
            start_row: int,
            start_col: int,
        ) -> bool:
            box_set: set[str] = set()
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    cell = board[i][j]
                    if cell != '.':
                        if cell in box_set:
                            return False
                        box_set.add(cell)
            return True

        def is_valid_board_boxes(board: List[List[str]]) -> bool:
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    if not is_valid_box(board, i, j):
                        return False
            return True

        return is_valid_board_lines(board) and is_valid_board_boxes(board)
