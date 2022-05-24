from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            current = arr[mid] - mid - 1
            if current < k:
                left = mid + 1
            else:
                right = mid - 1
        return left + k


sol = Solution()
ans = sol.findKthPositive([2, 3, 4, 7, 11], 5)
print(ans)
ans = sol.findKthPositive([1, 2, 3, 4], 2)
print(ans)
ans = sol.findKthPositive([2, 5, 6, 9, 11], 4)
print(ans)
ans = sol.findKthPositive([2], 1)
print(ans)
