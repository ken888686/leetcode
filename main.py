from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = False
        digits[len(digits) - 1] += 1
        for i in range(len(digits)-1, -1, -1):
            currentNum = digits[i] if not carry else digits[i]+1
            if currentNum > 9:
                digits[i] = currentNum % 10
                carry = True
            else:
                digits[i] = currentNum
                carry = False
                break
        if carry:
            digits.insert(0, 1)
        return digits


sol = Solution()
ans = sol.plusOne([9, 2, 9])
print(ans)
