from typing import List


class Solution:
    def twoSum(self, numberList: List[int], target: int) -> List[int]:
        indies = {}
        for i in range(len(numberList)):
            left = target-numberList[i]
            if left not in indies:
                indies[numberList[i]] = i
            else:
                return [indies[left], i]


sol = Solution()
print(sol.twoSum([9, 8, 2, 4, 3], 12))
