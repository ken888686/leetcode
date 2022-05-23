from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    island += 1
                    self.check(grid, i, j)
        return island

    def check(self, grid: List[List[str]], gr: int, gc: int) -> None:
        if gr < 0 or gr >= len(grid) or gc < 0 or gc >= len(grid[gr]) or grid[gr][gc] != "1":
            return
        grid[gr][gc] = "0"
        self.check(grid, gr+1, gc)
        self.check(grid, gr-1, gc)
        self.check(grid, gr, gc+1)
        self.check(grid, gr, gc-1)


sol = Solution()
ans = sol.numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
])
print(ans)
