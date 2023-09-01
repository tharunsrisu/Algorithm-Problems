'''
Excercise Statement
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorder(self,head,prev):
        if(prev.next.next==None):
            curr=prev.next
            secondNode=head.next
            head.next=curr
            curr.next=secondNode
            prev.next=None
            return secondNode
        else:
            output=self.reorder(head,prev.next)
            if(output!=None):
                if(output.next!=None):
                    if(output.next.next!=None):
                        anotherNode=output.next
                        curr=prev.next
                        output.next=curr
                        curr.next=anotherNode
                        prev.next=None
                        return output.next.next
                    else:
                        return output
                    
            
            
            
       
                
            
        
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        
        Input: [1,2,3,4,5,6]
        Output:[1,6,2,3,4,5]
        """
        if(head!=None):
            if(head.next!=None):
                if(head.next.next!=None):
                    self.reorder(head,head)
        return head