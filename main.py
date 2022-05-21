

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        left, right = 1, x
        result = 0
        while left <= right:
            mid = left+(right-left)//2
            if (x % mid == 0) and (x/mid == mid):
                return mid
            elif x/mid > mid:
                left = mid+1
                result = mid
            else:
                right = mid-1
        return result


sol = Solution()
ans = sol.mySqrt(48)
print(ans)
