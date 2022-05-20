class Solution:
    fib_cache = [0]*31

    def fib_DP_TopDown(self, n: int) -> int:
        if n <= 1:
            return n
        if self.fib_cache[n] != 0:
            return self.fib_cache[n]
        else:
            self.fib_cache[n] = \
                self.fib_DP_TopDown(n-1) + self.fib_DP_TopDown(n-2)
        return self.fib_cache[n]

    def fib_DP_BottomUp(self, n: int) -> int:
        if n <= 1:
            return n
        self.fib_cache[1] = 1
        for i in range(2, n+1):
            self.fib_cache[i] = \
                self.fib_cache[i-1] + self.fib_cache[i-2]
        return self.fib_cache[n]


sol = Solution()
print(sol.fib_DP_TopDown(5))
print(sol.fib_DP_BottomUp(5))
