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
        res = [root.val]
        stack = [root]
        while stack:
            nodes = []
            for node in stack:
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            if nodes:
                res.append(nodes[-1].val)
            stack = nodes
        return res

        