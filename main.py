from typing import List


class Solution:
    def searchInsert(self, numberList: List[int], target: int) -> int:
        left = 0
        right = len(numberList)-1
        while left <= right:
            mid = left + (right - left)//2
            if numberList[mid] == target:
                return mid
            if numberList[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


sol = Solution()
print(sol.searchInsert([1, 3, 5, 6], 9))
