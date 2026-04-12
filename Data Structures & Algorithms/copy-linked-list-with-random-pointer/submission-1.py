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
        hmap={}
        h=head
        while head:
            hmap[head] = Node(head.val,head.next,head.random)
            head = head.next
        for n in hmap.values():
            if n:
                if n.next:
                    n.next = hmap[n.next]
                if n.random:
                    n.random = hmap[n.random]
        return hmap[h] if h else None
        