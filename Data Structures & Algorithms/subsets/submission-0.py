class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def fun(i):

            if i>=len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[i])
            fun(i+1)
            curr.pop()
            fun(i+1)
        fun(0)
        return res

        

        