class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = 1+ count.get(i, 0)
        arr = [[] for i in range(len(nums)+1)]
        for key,val in count.items():
            arr[val].append(key)
        ans=[]
        for i in range(len(nums),0,-1):
            for j in arr[i]:
                ans.append(j)
                if len(ans)==k:
                    return ans
        
        