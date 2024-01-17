from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """Do not return anything, modify matrix in-place instead."""
        n = len(matrix)

        # Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row to get the final result
        for i in range(n):
            matrix[i].reverse()
