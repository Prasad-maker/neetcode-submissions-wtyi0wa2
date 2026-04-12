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
        oldtocur = defaultdict(lambda: Node(0))
        oldtocur[None] = None
        cur = head
        while cur:
            oldtocur[cur].val = cur.val
            oldtocur[cur].next = oldtocur[cur.next]
            oldtocur[cur].random = oldtocur[cur.random]
            cur = cur.next
        return oldtocur[head]
        