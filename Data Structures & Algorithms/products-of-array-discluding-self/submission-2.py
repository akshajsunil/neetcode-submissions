class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix =[1]
        p=1
        suffix=[]
        for i in range(1,len(nums)):
            p=nums[i-1]*p
            prefix.append(p)
            #print(p)
        p=1
        suffix.append(1)
        for i in range(len(nums),1,-1):
            p=nums[i-1]*p
            suffix.append(p)
            #print(p)
        
        arr =[]
        for i in range(len(nums)):
            arr.append(suffix[len(nums)-1-i]*prefix[i])
        return arr
        # 1 2 4 6
        # 1 1 2 8
        # 48 24 6



        