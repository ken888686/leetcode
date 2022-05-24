from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return self.twoPoints(numbers, target)

    def twoPoints(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            current = numbers[left] + numbers[right]
            if current == target:
                return [left+1, right+1]
            if current > target:
                right -= 1
            else:
                left += 1
        return [left+1, right+1]

    def hashmap(self, numbers: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(numbers)):
            current = target-numbers[i]
            if current in map:
                return [map[current]+1, i+1]
            map[numbers[i]] = i
        return [0, 0]


sol = Solution()
ans = sol.twoSum([2, 7, 11, 15], 9)
print(ans == [1, 2])
ans = sol.twoSum([2, 3, 4], 6)
print(ans == [1, 3])
ans = sol.twoSum([-1, 0], -1)
print(ans == [1, 2])
