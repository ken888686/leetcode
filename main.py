from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        length = len(citations)
        paper = [0] * (length + 1)
        for c in citations:
            paper[min(length, c)] += 1
        s, h = paper[-1], length
        while h > s:
            h -= 1
            s += paper[h]
        return h


sol = Solution()
data = [1, 3, 2]
ans = sol.hIndex(data)
print(ans)
