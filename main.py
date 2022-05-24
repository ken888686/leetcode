from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right, length = 0, len(citations)-1, len(citations)
        while left <= right:
            mid = left + (right - left) // 2
            if (length - mid) <= citations[mid]:
                right = mid-1
            else:
                left = mid+1
        return length - left


sol = Solution()
ans = [
    sol.hIndex([0, 1, 3, 5, 6, 7]),
    sol.hIndex([1, 2, 100]),
    sol.hIndex([1, 1]),
    sol.hIndex([1]),
    sol.hIndex([0])
]
print(ans)
