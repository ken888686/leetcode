from typing import List


class Solution:
    def sortedSquares(self, numberList: List[int]) -> List[int]:
        result = [0]*len(numberList)
        left, right = 0, len(numberList)-1
        while left <= right:
            leftNum, rightNum = abs(numberList[left]), abs(numberList[right])
            if leftNum > rightNum:
                result[right-left] = leftNum**2
                left += 1
            else:
                result[right-left] = rightNum**2
                right -= 1
        return result


sol = Solution()
print(sol.sortedSquares([-9, -4, -2, -1, 0, 3, 5, 9, 10]))
