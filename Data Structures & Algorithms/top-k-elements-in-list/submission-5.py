class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d :
                d[i]+=1
            else:
                d[i]=1
        d1 = [[] for i in range(len(nums)+1) ]
        
        for kv,v in d.items():
            
            d1[v].append(kv)

        
        ans = []
        d2 = d1[::-1]
        for i in d2:
            for j in i:
                if len(i) !=0 and k!=0:
                    ans.append(j)
                    k-=1
                if k==0:
                    break
            if k==0:
                    break

           
        

        return ans
            

        