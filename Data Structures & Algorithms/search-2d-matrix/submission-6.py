class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lr,rr=0,len(matrix)-1
        while(lr<=rr):
            m=(lr+rr)//2
            if matrix[m][0]>target:
                rr-=1
            elif matrix[m][-1]<target: 
                lr+=1
            else: 
                R=m
                break
        if not (lr <=rr):
            return False
        lc,rc = 0,len(matrix[0])
        while(lc<=rc):
            m=(lc+rc)//2
            if matrix[R][m]==target:
                return True
            elif matrix[R][m]>target:
                rc-=1
            else:lc+=1
        return False
        


        