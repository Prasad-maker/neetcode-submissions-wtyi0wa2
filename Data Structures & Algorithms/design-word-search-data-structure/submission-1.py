class TriNode:
    def __init__(self):
        self.children={}
        self.eow = False
class WordDictionary:

    def __init__(self):
        self.root = TriNode()
        

    def addWord(self, word: str) -> None:
        cur= self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] =TriNode()
            cur = cur.children[c]
        cur.eow = True
    def search(self, word: str) -> bool:
        def dfs(j,root):
            cur= root
            for i in range(j,len(word)):
                c=word[i]
                if c!=".":
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
                else:
                    for child in cur.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
            
            return cur.eow
        return dfs(0,self.root)
        
