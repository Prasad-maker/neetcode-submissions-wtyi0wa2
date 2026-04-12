class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            hmap = set()
            for j in range(9):
                if board[i][j]!=".":
                    if board[i][j] in hmap:
                        return False
                    hmap.add(board[i][j])
        for i in range(9):
            hmap = set()
            for j in range(9):
                if board[j][i]!=".":
                    if board[j][i] in hmap:
                        return False
                    hmap.add(board[j][i])
        for i in range(3):
            for j in range(3):
                hmap = set()
                for k in range(3):
                    for l in range(3):
                        r=3*i+k
                        c=3*j+l
                        if board[r][c]!=".":
                            if board[r][c] in hmap:
                                return False
                            hmap.add(board[r][c])
        return True
                
        