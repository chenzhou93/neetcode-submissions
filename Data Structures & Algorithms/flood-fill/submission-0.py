class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        color_value = image[sr][sc]
        self.dfs(image, sr, sc, color, color_value)
        return image
    
    def dfs(self, image, r, c, color, color_value):
        ROW, COL = len(image), len(image[0])

        if(
            min(r, c) < 0
            or r == ROW
            or c == COL
            or image[r][c] != color_value
            or image[r][c] == color
        ):
            return
        
        image[r][c] = color
        
        self.dfs(image, r + 1, c, color, color_value)
        self.dfs(image, r - 1, c, color, color_value)
        self.dfs(image, r, c + 1, color, color_value)
        self.dfs(image, r, c - 1, color, color_value)
        
