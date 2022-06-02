from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        result = [[None] * row for _ in range(col)]
        for i in range(row):
            for j in range(col):
                result[j][i] = matrix[i][j]
        return result


sol = Solution()
ans = sol.transpose([[1, 2, 3], [4, 5, 6]])
print(ans)
