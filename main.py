from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while numbers[left]+numbers[right] != target:
            if numbers[left]+numbers[right] < target:
                left += 1
            else:
                right -= 1
        return [left+1, right+1]


sol = Solution()
print(sol.twoSum([2, 5, 7, 11, 15], 9))
