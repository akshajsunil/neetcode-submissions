# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return [] 
        l = []
        dq = deque()
        dq.appendleft(root)
        while(len(dq)>0):
            l1 =[]
            a=0
            for i in range(len(dq)):
                curr = dq.pop()
                a=curr.val
                if curr.left:
                    dq.appendleft(curr.left)
                if curr.right:
                    dq.appendleft(curr.right)
                
            l.append(a)
        return l