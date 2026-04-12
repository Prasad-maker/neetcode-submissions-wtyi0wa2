class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0,len(matrix)-1
        R=-1
        while l <=r:
            m= (l+r)//2
            if matrix[m][0]<= target<= matrix[m][-1]:
                R = m
                break
            elif target<matrix[m][0]:
                r=m-1
            else:
                l=m+1
        if R==-1: return False
        l,r = 0,len(matrix[0])-1
        while l <=r:
            m= (l+r)//2
            if matrix[R][m]== target:
                return True
            elif target<matrix[R][m]:
                r=m-1
            else:
                l=m+1
        return False
            
