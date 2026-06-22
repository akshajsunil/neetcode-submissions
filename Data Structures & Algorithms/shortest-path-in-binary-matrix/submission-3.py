class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid) , len(grid[0])
        if grid[0][0] == 1:
            return -1

        visited = set()
        visited.add((0,0))
        queue = deque()
        queue.append((0,0))
        length =0
        while queue:
            length+=1
            for i in range(len(queue)):
                r,c = queue.popleft()
                if r==ROWS-1 and c == COLS-1:
                    return length
                
                are = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]
                for dr , dc in are:
                    ir = dr+r
                    ic = dc+c
                    if min(ir,ic)<0 or ir==ROWS or ic==COLS or (ir,ic) in visited or grid[ir][ic]==1:
                        continue
                    visited.add((ir,ic))
                    queue.append((ir,ic))
            
        
        return -1




        