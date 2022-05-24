class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right, ans = 1, n, 0
        while left < right:
            mid = left + (right - left)//2
            current = (mid*(mid-1))//2
            if current > n:
                right = mid
            else:
                ans = left
                left = mid + 1
        return ans


sol = Solution()
ans = sol.arrangeCoins(20)
print(ans)
