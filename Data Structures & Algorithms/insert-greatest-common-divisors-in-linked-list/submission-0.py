# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        def gcd(i,j):
            while j>0:
                i,j = j, i%j
            return i
        while cur.next:
            n1,n2 = cur.val,cur.next.val
            cur.next = ListNode(gcd(n1,n2),cur.next)
            cur = cur.next.next
        return head





        