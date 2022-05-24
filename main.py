class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n <= 1:
            return n
        if n <= 3:
            return 2 if n == 3 else 1
        left, right = 1, n
        while left < right:
            mid = left + (right - left)//2
            current = (mid*(mid+1))//2
            if current > n:
                right = mid
            else:
                left = mid + 1
        return left - 1


sol = Solution()
ans = sol.arrangeCoins(8)
print(ans)
