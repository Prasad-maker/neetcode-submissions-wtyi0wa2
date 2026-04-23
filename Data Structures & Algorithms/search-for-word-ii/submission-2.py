class TriNode:
    def __init__(self):
        self.children = {}
        self.word = ""
    def addword(self,word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TriNode()
            cur = cur.children[c]
        cur.word = word
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TriNode()
        for w in words:
            root.addword(w)
        ROWS,COLS = len(board), len(board[0])
        res = set()
        def dfs(r,c,node):
            if (r<0 or c<0 or r>=ROWS or c>=COLS or board[r][c] not in node.children):
                return
            node = node.children[board[r][c]]
            ch = board[r][c]
            if node.word:
                res.add(node.word)
                node.word = ""
            if node.children:
                board[r][c] = "#"
                dfs(r+1,c,node)
                dfs(r-1,c,node)
                dfs(r,c-1,node)
                dfs(r,c+1,node)
                board[r][c] = ch
                
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root)
        return list(res)


        