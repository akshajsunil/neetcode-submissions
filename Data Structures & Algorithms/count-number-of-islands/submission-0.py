class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW,COL = len(grid) , len(grid[0])
        no=2
        ss = set()


        def ff(r,c):
            
            
            if r>=ROW or c>=COL or min(r,c)<0 or (r,c) in ss or grid[r][c]!="1":
                return
            ss.add((r,c))

            grid[r][c] = str(no)

            ff(r+1,c)
            ff(r,c+1)
            ff(r-1,c)
            ff(r,c-1)

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] =="1" :
                    no=no+1
                    ff(i,j)
                    ss = set()
        for i in range(ROW):
            for j in range(COL):
                print(f"{i} {j} : {grid[i][j]}")
                    

        return no-2
        