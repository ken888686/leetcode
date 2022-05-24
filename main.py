class Solution:
    def checkRecord(self, s: str) -> bool:
        a = l = 0
        for c in s:
            if c == "A":
                a += 1
            if c == "l":
                l += 1
            else:
                l = 0
            if a >= 2 or l >= 3:
                return False
        return True


sol = Solution()
ans = sol.checkRecord("AA")
print(ans)
