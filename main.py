from typing import List


class Solution:
    def reverse(self, s: str) -> str:
        left = 0
        right = len(s)-1
        s = list(s)
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)

    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        for i in range(len(s)):
            s[i] = self.reverse(s[i])
        return ' '.join(s)


sol = Solution()
print(sol.reverseWords('Let\'s take LeetCode contest'))
