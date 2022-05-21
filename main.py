import collections
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        current = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                current = max(current, prices[right]-prices[left])
            else:
                left = right
            right += 1
        return current


sol = Solution()
ans = sol.maxProfit([7, 5, 3, 1, 7, 1, 8, 6, 9])
print(ans)
