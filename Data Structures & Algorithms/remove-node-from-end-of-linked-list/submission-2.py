# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        i = 0
        while node and i<n:
            node = node.next
            i+=1
        start =dummy =  ListNode(0,head)
        end = node
        while end:
            start = start.next
            end = end.next
        
        start.next = start.next.next
        return dummy.next
        
        