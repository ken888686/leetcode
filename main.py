from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))


sol = Solution()
ans = sol.maximumWealth([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(ans)
