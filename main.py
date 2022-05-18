from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(numbers)):
            if target-numbers[i] in map:
                return [map[target-numbers[i]]+1, i+1]
            map[numbers[i]] = i


sol = Solution()
print(sol.twoSum([2, 5, 7, 11, 15], 9))
