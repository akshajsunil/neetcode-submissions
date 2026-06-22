class KthLargest:
    
    

    def __init__(self, k: int, nums: List[int]):
        self.heap =[]
        
        self.kth = k
        for i in nums:
            heapq.heappush(self.heap,i)
        while len(self.heap)>k:
            heapq.heappop(self.heap)

        
    
    def add(self, val: int) -> int:
        
        heapq.heappush(self.heap,val)
        if self.kth<len(self.heap):
            heapq.heappop(self.heap)
        return self.heap[0]
        


        
