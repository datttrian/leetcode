class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights: list[int] = [0] * cols
        max_area = 0

        for i in range(rows):
            # Update the heights array based on the current row
            for j in range(cols):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0

            # Calculate the maximum area for the current row
            stack: list[int] = []
            for j in range(cols + 1):
                while stack and (j == cols or heights[j] < heights[stack[-1]]):
                    height = heights[stack.pop()]
                    width = stack[-1] if stack else -1
                    max_area = max(max_area, height * (j - width - 1))
                stack.append(j)

        return max_area
