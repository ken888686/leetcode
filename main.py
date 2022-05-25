from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        length = len(original)
        ans = [[None] * n for _ in range(m)]
        if length != m*n:
            return []
        for i in range(length):
            ans[i // n][i % n] = original[i]
        return ans


sol = Solution()
ans = sol.construct2DArray(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    5,
    2)
print(ans)
