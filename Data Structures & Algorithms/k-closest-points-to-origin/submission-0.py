class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = {}
        l = []
        for i in points:
            v = i[0]*i[0]+i[1]*i[1]
            l.append(v)
            if v not in d:
                d[v]=[]
            d[v].append(i)
        heapq.heapify(l)
        n=[]
        while k!=0:
            mi = heapq.heappop(l)
            mi = d[mi]
            if len(mi)>k:
                n = n+mi[:k]
            else:
                k = k - len(mi)
                n = n+mi
            
        return n

        