class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS,COLS = len(matrix),len(matrix[0])
        row1 = False
        for i in range(COLS):
            if matrix[0][i]==0:
                row1 = True
        for i in range(1,ROWS):
            for j in range(COLS):
                if matrix[i][j] ==0:
                    matrix[i][0]=0
                    matrix[0][j] =0
        for i in range(1,ROWS):
            for j in range(1,COLS):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if matrix[0][0] == 0:
            for i in range(1,ROWS):
                matrix[i][0]=0
        if row1:
            for j in range(COLS):
                matrix[0][j] = 0


        