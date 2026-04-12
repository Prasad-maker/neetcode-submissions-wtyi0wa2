class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqs =defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]!=".":
                    if (board[r][c] in rows[r]) or (board[r][c] in cols[c]) or (board[r][c] in sqs[(r//3,c//3)]):
                        return False
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    sqs[(r//3,c//3)].add(board[r][c])
        return True


        