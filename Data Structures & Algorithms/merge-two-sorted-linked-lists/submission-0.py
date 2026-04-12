# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1,head2=list1,list2
        h=head = ListNode()
        while head1 or head2:
            if head1 and head2:
                if head1.val<=head2.val:
                    head.next = head1
                    head1=head1.next
                else:
                    head.next = head2
                    head2=head2.next
                head = head.next
            elif head1:
                head.next = head1
                head1=None
            elif head2:
                head.next = head2
                head2=None
        return h.next
            


        