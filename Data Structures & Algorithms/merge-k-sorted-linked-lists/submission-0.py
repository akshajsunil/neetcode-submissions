# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge(self,l1,l2):
        if l1 ==None and l2 ==None:
            return None
        if l1 ==None:
            return None
        if l2==None:
            return None
        if l1.val>l2.val:
            l3=l2
            l2=l2.next
        else:
            l3=l1
            l1=l1.next
        l4 =l3
        while l1!=None and l2!=None:
            if l1.val>l2.val:
                l3.next = l2
                l2=l2.next
                l3=l3.next
            else:
                l3.next = l1
                l1 = l1.next
                l3=l3.next
        if l1!=None:
            l3.next=l1
        if l2!=None:
            l3.next = l2
        return l4 


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return 
        l = len(lists)
        if l <=1:
            return lists[0]
        m = l//2
        a = self.mergeKLists(lists[:m])
        b = self.mergeKLists(lists[m:])
        return self.merge(a,b)
        