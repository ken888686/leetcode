from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        start = 0
        end = len(s)-1
        while start <= end:
            s[start], s[end] = s[end], s[start]
            start, end = start+1, end-1
        print(s)


sol = Solution()
sol.reverseString(["h", "e", "l", "l", "o"])
