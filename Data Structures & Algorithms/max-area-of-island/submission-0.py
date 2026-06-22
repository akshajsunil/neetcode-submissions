class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW ,COL = len(grid) , len(grid[0])
        count=0
        maxcount=0

        def ff(r,c):
            nonlocal count
            if r>=ROW or c>=COL or min(r,c)<0 or grid[r][c]!=1:
                return
            count=count+1
            grid[r][c]=0
            ff(r+1,c)
            ff(r,c+1)
            ff(r,c-1)
            ff(r-1,c)
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j]==1:
                    count=0
                    ff(i,j)
                    maxcount = max(count,maxcount)
        return maxcount
                
        