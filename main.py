class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        result = 0
        start = 0
        for i in range(len(s)):
            if s[i] in map:
                start = max(map[s[i]]+1, start)
            result = max(result, i - start + 1)
            map[s[i]] = i
        return result


sol = Solution()
print(sol.lengthOfLongestSubstring("dvdf"))
