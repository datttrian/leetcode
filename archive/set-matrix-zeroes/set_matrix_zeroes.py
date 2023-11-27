class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """Do not return anything, modify matrix in-place instead."""
        if not matrix or not matrix[0]:
            return

        rows, cols = len(matrix), len(matrix[0])
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))

        # Use the first row and first column to mark if the corresponding row
        # or column should be set to zero
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        # Set zeros based on markings in the first row and first column
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Set zeros for the first row and first column if necessary
        if first_row_has_zero:
            for j in range(cols):
                matrix[0][j] = 0

        if first_col_has_zero:
            for i in range(rows):
                matrix[i][0] = 0
