class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res: list[int] = []

        if not matrix or not matrix[0]:
            return res

        row_begin, row_end, col_begin, col_end = (
            0,
            len(matrix) - 1,
            0,
            len(matrix[0]) - 1,
        )

        while row_begin <= row_end and col_begin <= col_end:
            for j in range(col_begin, col_end + 1):
                res.append(matrix[row_begin][j])
            row_begin += 1

            for j in range(row_begin, row_end + 1):
                res.append(matrix[j][col_end])
            col_end -= 1

            if row_begin <= row_end:
                for j in range(col_end, col_begin - 1, -1):
                    res.append(matrix[row_end][j])
                row_end -= 1

            if col_begin <= col_end:
                for j in range(row_end, row_begin - 1, -1):
                    res.append(matrix[j][col_begin])
                col_begin += 1

        return res
