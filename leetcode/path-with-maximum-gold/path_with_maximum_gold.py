class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        def dfs(x: int, y: int) -> int:
            if (
                x < 0
                or x >= len(grid)
                or y < 0
                or y >= len(grid[0])
                or grid[x][y] == 0
            ):
                return 0

            current_gold = grid[x][y]
            grid[x][y] = 0

            max_gold = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                max_gold = max(max_gold, dfs(x + dx, y + dy))

            grid[x][y] = current_gold

            return current_gold + max_gold

        max_gold_collected = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell != 0:
                    max_gold_collected = max(max_gold_collected, dfs(i, j))

        return max_gold_collected
