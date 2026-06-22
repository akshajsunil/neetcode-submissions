# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minNode(self,root):
        curr = root
        while curr.left !=None:
            curr = curr.left
        return curr
    
            
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right,key)
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        else:

            if root.left ==None:
                return root.right
            elif root.right ==None:
                return root.left
            else:
                t = self.minNode(root.right)
                root.val = t.val
                root.right  = self.deleteNode(root.right,t.val)
        return root
        