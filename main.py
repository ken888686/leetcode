class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num
        while left <= right:
            mid = left+(right-left)//2
            if num % mid == 0 and num//mid == mid:
                return True
            if (num/mid) < mid:
                right = mid-1
            else:
                left = mid+1
        return False


sol = Solution()
print(sol.isPerfectSquare(1))
