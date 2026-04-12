"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        curr = head
        while head:
            temp = head.random
            head.random = Node(head.val,None,temp)
            head = head.next
        copy = curr.random
        while curr and curr.next:
            curr.random.next = curr.next.random
            curr = curr.next
        head = copy
        while head:
            if head.random:
                head.random = head.random.random
            head = head.next
        return copy
        