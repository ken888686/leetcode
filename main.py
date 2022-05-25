from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        ans = [[None]*c for _ in range(r)]
        matCol = len(mat[0])
        for i in range(r*c):
            ans[i // c][i % c] = mat[i // matCol][i % matCol]
        return ans


sol = Solution()
ans = sol.matrixReshape(
    [[0]],
    1,
    1)
print(ans)
