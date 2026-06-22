class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        l = -200
        for i in range(0,len(nums)):
            if(l<nums[i]):
                nums[k]=nums[i]
                l=nums[i]
                k+=1
        return k

