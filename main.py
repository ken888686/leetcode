

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        left, right, result = 1, x, 0
        while left <= right:
            mid = left+(right-left)//2
            if (x % mid == 0) and (x/mid == mid):
                return mid
            if x/mid > mid:
                left = mid+1
                result = mid
            else:
                right = mid-1
        return result


sol = Solution()
ans = sol.mySqrt(120)
print(ans)
