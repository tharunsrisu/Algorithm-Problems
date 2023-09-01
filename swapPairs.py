# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=head
        b=head.next
        if(b==None):
            return head
        c=b.next
        head=head.next
        a.next=None
        head.next=a
        if(c==None):
            
            return head
        head.next.next=self.swapPairs(c)
        return head