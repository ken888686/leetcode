class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        strList = list(s)
        start = 0
        end = len(s)-1
        while start < end:
            if s[start] in vowels and s[end] in vowels:
                strList[start], strList[end] = s[end], s[start]
            elif s[start] in vowels:
                end -= 1
                continue
            elif s[end] in vowels:
                start += 1
                continue
            start, end = start+1, end-1
        return ''.join(strList)


sol = Solution()
print(sol.reverseVowels("initial"))
