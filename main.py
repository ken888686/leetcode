from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    ans += 1 if self.dfs(grid, i, j) else 0
        return ans

    def dfs(self, grid: List[List[int]], row: int, col: int) -> bool:
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return False
        if grid[row][col] == 1:
            return True
        grid[row][col] = 1
        d1 = self.dfs(grid, row+1, col)
        d2 = self.dfs(grid, row-1, col)
        d3 = self.dfs(grid, row, col+1)
        d4 = self.dfs(grid, row, col-1)
        return d1 and d2 and d3 and d4


sol = Solution()
ans = sol.closedIsland([
    [0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
    [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
    [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]
])
print(ans)
