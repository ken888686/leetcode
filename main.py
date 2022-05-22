from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        self.fill(image, sr, sc, image[sr][sc], newColor)
        return image

    def fill(self, image: List[List[int]], sr: int, sc: int, color: int, newColor: int) -> None:
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[sr]) or image[sr][sc] != color:
            return
        image[sr][sc] = newColor
        self.fill(image, sr+1, sc, color, newColor)
        self.fill(image, sr, sc+1, color, newColor)
        self.fill(image, sr-1, sc, color, newColor)
        self.fill(image, sr, sc-1, color, newColor)


sol = Solution()
ans = sol.floodFill(
    image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]],
    sr=1,
    sc=1,
    newColor=2)
print(ans)
