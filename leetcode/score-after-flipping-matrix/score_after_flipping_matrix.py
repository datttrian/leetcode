class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:

        for row in grid:
            if row[0] == 0:
                for j in range(len(row)):
                    row[j] = 1 - row[j]

        for j in range(1, len(grid[0])):
            num_ones = sum(row[j] for row in grid)
            if num_ones < len(grid) / 2:
                for row in grid:
                    row[j] = 1 - row[j]

        total_score = 0
        for row in grid:
            row_value = int("".join(map(str, row)), 2)
            total_score += row_value

        return total_score
