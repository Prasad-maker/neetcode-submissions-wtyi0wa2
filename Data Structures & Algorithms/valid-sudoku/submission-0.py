class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqs = defaultdict(set)
        for c in range(9):
            for r in range(9):
                if board[r][c]==".":
                    continue
                if (board[r][c] in rows[r]) or (board[r][c] in sqs[(r//3,c//3)]) or (board[r][c] in cols[c]):
                    return False
            
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                sqs[(r//3,c//3)].add(board[r][c])
        return True


        