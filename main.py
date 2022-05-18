from typing import List


class Solution:
    def moveZeroes(self, numbers: List[int]) -> None:
        left = 0
        for i in range(len(numbers)):
            if numbers[left] == 0 and numbers[i] != 0:
                numbers[left], numbers[i] = numbers[i], numbers[left]
            if numbers[left] != 0:
                left += 1
        print(numbers)


sol = Solution()
print(sol.moveZeroes([1, 2, 0, 3, 4, 0, 5, 6, 7, 8, 0]))
