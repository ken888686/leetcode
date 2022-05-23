from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        maxLand = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    maxLand = max(maxLand, self.dfs(grid, i, j))
        return maxLand

    def dfs(self, grid: List[List[int]], gr: int, gc: int) -> int:
        if gr < 0 or gr >= len(grid) or gc < 0 or gc >= len(grid[gr]) or grid[gr][gc] != 1:
            return 0
        grid[gr][gc] = 0
        return 1 \
            + self.dfs(grid, gr+1, gc) \
            + self.dfs(grid, gr-1, gc) \
            + self.dfs(grid, gr, gc+1) \
            + self.dfs(grid, gr, gc-1)

    def bfs(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0

        gr, gc = len(grid), len(grid[0])
        queue, max_area = deque([]), 0

        def _bfs(queue: deque) -> int:
            cur_area = 1
            while queue:
                i, j = queue.popleft()
                for ni, nj in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                    if 0 <= ni < gr and 0 <= nj < gc and grid[ni][nj] == 1:
                        grid[ni][nj] = 0
                        cur_area += 1
                        queue.append((ni, nj))
            return cur_area

        for i in range(gr):
            for j in range(gc):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    queue.append([i, j])
                    max_area = max(max_area, _bfs(queue))
        return max_area


sol = Solution()
ans = sol.bfs([
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
])
print(ans)
