class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        for row in grid:
            if row[0] == 0:
                for j in range(len(row)):
                    row[j] ^= 1

        for col in range(1, len(grid[0])):
            num_ones = sum(row[col] for row in grid)
            if num_ones < len(grid) / 2:
                for row in grid:
                    row[col] ^= 1

        score = 0
        for row in grid:
            row_value = int("".join(map(str, row)), 2)
            score += row_value

        return score
