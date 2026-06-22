# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        

        dq = deque()
        dq.appendleft(root)
        l=[]
        while len(dq)>0:
            l1 =[]
            for i in range(len(dq)):
                
                curr = dq.pop()
                l1.append(curr.val)
                if curr.left:
                    dq.appendleft(curr.left)
                if curr.right:
                    dq.appendleft(curr.right)
            l.append(l1)
        return l

                


