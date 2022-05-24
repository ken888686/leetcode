from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        counter = 1
        for i in range(len(citations)-1, -1, -1):
            if citations[i] >= counter:
                counter += 1
        return counter - 1


sol = Solution()
ans = sol.hIndex([1, 0, 4, 6, 3])
print(ans)
ans = sol.hIndex([1, 2, 100])
print(ans)
ans = sol.hIndex([1, 1])
print(ans)
ans = sol.hIndex([0])
print(ans)
