from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)


sol = Solution()
ans = sol.singleNumber([1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7, 8, 9, 7, 8, 9])
print(ans)
