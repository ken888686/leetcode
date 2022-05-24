from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ans = 0
        row = len(grid)
        col = len(grid[0])
        if not row or not col:
            return 0

        for i in range(row):
            for j in range(col):
                if i == 0 or i == row-1 or j == 0 or j == col-1:
                    self.dfs(grid, i, j)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    ans += 1
        return ans

    def dfs(self, grid: List[List[int]], row: int, col: int) -> int:
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col]:
            grid[row][col] = 0
            for i, j in [[row+1, col], [row-1, col], [row, col+1], [row, col-1]]:
                self.dfs(grid, i, j)


sol = Solution()
grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]
ans = sol.numEnclaves(grid)
print(ans)
