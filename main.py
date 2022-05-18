from typing import List


class Solution:
    def reverse(self, numberList: List[int], left: int, right: int):
        print(f"numberList:{numberList}, left:{left}, right:{right}")
        while left <= right:
            numberList[left], numberList[right] = numberList[right], numberList[left]
            left += 1
            right -= 1

    def rotate(self, numberList: List[int], k: int) -> List[int]:
        k %= len(numberList)
        if k == 0:
            return numberList
        self.reverse(numberList, 0, len(numberList)-k-1)
        self.reverse(numberList, len(numberList)-k, len(numberList)-1)
        self.reverse(numberList, 0, len(numberList)-1)
        return numberList


sol = Solution()
print(sol.rotate([1, 2, 3, 4, 5], 2))
