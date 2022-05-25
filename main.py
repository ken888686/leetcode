from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = [False] * (len(s) + 1)
        d[0] = True
        for i in range(len(s)+1):
            for j in range(i):
                if d[j] and s[j:i] in wordDict:
                    d[i] = True
                    break
        return d[len(s)]


sol = Solution()
ans = sol.wordBreak(s="applepencil", wordDict=["apple", "pencil"])
print(ans)
ans = sol.wordBreak(s="a", wordDict=["a"])
print(ans)
