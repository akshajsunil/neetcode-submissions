class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW,COL = len(grid) , len(grid[0])
        no=0


        def ff(r,c):
            
            
            if r>=ROW or c>=COL or min(r,c)<0  or grid[r][c]!="1":
                return

            grid[r][c] = 0

            ff(r+1,c)
            ff(r,c+1)
            ff(r-1,c)
            ff(r,c-1)

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] =="1" :
                    no=no+1
                    ff(i,j)
        for i in range(ROW):
            for j in range(COL):
                print(f"{i} {j} : {grid[i][j]}")
                    

        return no
        