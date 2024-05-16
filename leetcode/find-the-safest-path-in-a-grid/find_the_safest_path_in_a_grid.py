from collections import deque
import heapq
from typing import Tuple


class Solution:
    row_directions = [0, 0, -1, 1]
    col_directions = [-1, 1, 0, 0]

    def bfs(
        self, grid: list[list[int]], scores: list[list[float]], n: int
    ) -> None:
        queue: deque[Tuple[int, int]] = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    scores[i][j] = 0
                    queue.append((i, j))

        while queue:
            x, y = queue.popleft()
            current_score = scores[x][y]

            for i in range(4):
                new_x = x + self.row_directions[i]
                new_y = y + self.col_directions[i]

                if (
                    0 <= new_x < n
                    and 0 <= new_y < n
                    and scores[new_x][new_y] > current_score + 1
                ):
                    scores[new_x][new_y] = current_score + 1
                    queue.append((new_x, new_y))

    def maximumSafenessFactor(self, grid: list[list[int]]) -> float:
        n: int = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return 0

        scores: list[list[float]] = [[float("inf")] * n for _ in range(n)]
        self.bfs(grid, scores, n)

        visited: list[list[bool]] = [[False] * n for _ in range(n)]
        priority_queue: list[Tuple[float, int, int]] = [(-scores[0][0], 0, 0)]
        heapq.heapify(priority_queue)

        while priority_queue:
            current_safe, x, y = heapq.heappop(priority_queue)
            current_safe = -current_safe

            if x == n - 1 and y == n - 1:
                return current_safe

            visited[x][y] = True

            for i in range(4):
                new_x = x + self.row_directions[i]
                new_y = y + self.col_directions[i]

                if (
                    0 <= new_x < n
                    and 0 <= new_y < n
                    and not visited[new_x][new_y]
                ):
                    new_safe = min(current_safe, scores[new_x][new_y])
                    heapq.heappush(priority_queue, (-new_safe, new_x, new_y))
                    visited[new_x][new_y] = True

        return -1
