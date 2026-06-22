class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        l = []
        for i in stones:
            l.append(-i)
        
        heapq.heapify(l)
        while len(l)>1:
            n1 = -heapq.heappop(l)
            n2 = -heapq.heappop(l)
            if n1==n2:
                continue
            else:
                heapq.heappush(l,-abs(n1-n2))
        if len(l) == 0:
            return 0
        return -heapq.heappop(l)
        

        