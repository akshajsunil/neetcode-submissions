class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=1
        arr=[]
        if 0 not in nums:
            for i in nums:

                p=p*i
            for i in nums:
                arr.append(int(p/i))
            return arr
        else:
            c=0
            ids=0
            for i in range(len(nums)):
                if nums[i] ==0:
                    c+=1
                    ids=i
                    if c==2:
                        return [0]*len(nums)
                else:
                    p=p*nums[i]
            arr=[0]*len(nums)
            arr[ids]=p
            return arr

        
        