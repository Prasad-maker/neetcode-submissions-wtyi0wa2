class TriNode:
    def __init__(self):
        self.children= {}
        self.isword = False
    def addword(self,word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TriNode()
            cur = cur.children[c]
        cur.isword= True
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TriNode()
        for w in words:
            root.addword(w)

        ROWS,COLS=len(board),len(board[0])
        res,visit = set(),set()
        def dfs(r,c,node,word):
            if (r==ROWS or c==COLS or r<0 or c<0 or (r,c) in visit or
                board[r][c]not in node.children):
                return
            visit.add((r,c))
            node = node.children[board[r][c]]
            word+=board[r][c]
            if node.isword:
                res.add(word)
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visit.remove((r,c))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")
        return list(res)


        