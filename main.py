from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        currentShifts = 0
        s = list(s)
        for i in range(len(s)-1, -1, -1):
            currentShifts = (currentShifts + shifts[i]) % 26
            s[i] = chr((ord(s[i]) - ord('a') + currentShifts) % 26 + ord('a'))
        return ''.join(s)


sol = Solution()
print(sol.shiftingLetters('abc', [1, 1, 24]))
