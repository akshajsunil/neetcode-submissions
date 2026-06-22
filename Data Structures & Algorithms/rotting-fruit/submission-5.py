class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        visited = set()
        queue = deque()
        noRotten = 0
        noFresh = 0
        length=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==2:
                    noRotten +=1
                    queue.append((r,c))
                    visited.add((r,c))
                if grid[r][c]==1:
                    noFresh+=1
        if noFresh ==0:
            return 0
        if noRotten ==0:
            return -1
        while queue:
            
            for i in range(len(queue)):
                r,c = queue.popleft()
                
                if grid[r][c]==1:
                    grid[r][c]=2
                    noFresh-=1
                    
                way = [(0,1),(1,0),(-1,0),(0,-1)]
                for dr , dc in way:
                    ir = r+dr
                    ic = c+dc
                    if min(ir,ic)<0 or ir == ROWS or ic ==COLS or (ir,ic) in visited or grid[ir][ic]==0:
                        continue
                    queue.append((ir,ic))
                    visited.add((ir,ic))
            if noFresh==0:
                    return length
            length+=1
            
        return -1