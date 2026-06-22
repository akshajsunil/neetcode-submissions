# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val)
        t =root
        while t!=None:
        
            if t.val>val:
                if t.left ==None:
                    t.left = TreeNode(val)
                    break
                t = t.left
            elif t.val<val:
                if t.right ==None:
                    t.right = TreeNode(val)
                    break
                t = t.right
        return root