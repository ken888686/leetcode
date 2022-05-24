from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 1:
            return [-1, -1]
        first = self.firstPosition(nums, target)
        last = self.lastPosition(nums, target)
        return [first, last]

    def firstPosition(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right - left)//2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid+1
        return left if nums[left] == target else -1

    def lastPosition(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right - left + 1)//2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid-1
        return left if nums[right] == target else -1


sol = Solution()
ans = sol.searchRange(
    [5, 5, 5, 5, 5,
     7, 7, 7, 8, 8,
     8, 8, 9, 9, 9,
     9, 9, 9, 9, 9],
    6)
print(ans)
