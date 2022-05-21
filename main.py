from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters)
        while left < right:
            mid = left + (right - left)//2
            if ord(letters[mid]) <= ord(target):
                left = mid + 1
            else:
                right = mid
        return letters[left % len(letters)]


sol = Solution()
ans = sol.nextGreatestLetter(
    letters=["c", "d", "f", "g", "i", "j"],
    target="j")
print(ans)
