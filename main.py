from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix


sol = Solution()
ans = sol.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(ans)
