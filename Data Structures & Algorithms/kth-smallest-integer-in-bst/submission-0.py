# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def fun(self,root,k,l):
        if root is None:
            return
        
        self.fun(root.left,k,l)
        l.append(root.val)
        if len(l) == k :
            return
        self.fun(root.right,k,l)
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l = []
        self.fun(root,k,l)
        return l[k-1]
        