class Solution:
    def check(self,piles,n,h):
        
        su=0
        for i in piles:
            if i%n==0:
                su = su+i//n
            else:
                su = su+i//n+1
            
        return su<=h
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1 
        # max(piles)
        left =1 
        right = max(piles)
        while left<=right:
            mid = (left+right)//2

            if not self.check(piles,mid,h):
                left = mid+1
            else:
                right = mid-1
        return left
        