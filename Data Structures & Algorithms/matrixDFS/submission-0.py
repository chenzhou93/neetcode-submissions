class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visit = set()
        return self.dfs(grid, 0, 0, visit)
    
    def dfs(self, grid, r, c, visit):
        ROW, COL = len(grid), len(grid[0])

        if (
            min(r, c) < 0 
            or (r, c) in visit
            or r == ROW
            or c == COL
            or grid[r][c] == 1
        ):
            return 0
        
        if r == ROW - 1 and c == COL - 1:
            return 1
        
        visit.add((r, c))
        
        count = 0
        count += self.dfs(grid, r-1, c, visit)
        count += self.dfs(grid, r+1, c, visit)
        count += self.dfs(grid, r, c-1, visit)
        count += self.dfs(grid, r, c+1, visit)
        
        visit.remove((r, c))

        return count


        