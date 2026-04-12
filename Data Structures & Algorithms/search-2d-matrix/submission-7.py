class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0 , len(matrix)-1
        R,C = len(matrix),len(matrix[0])
        while r>=l:
            M= (r+l)//2
            if matrix[M][0]<=target<=matrix[M][-1]:
                break
            elif matrix[M][0]>target:
                r=M-1
            else:
                l=M+1
        l,r = 0,C-1
        while r>=l:
            m = (r+l)//2
            if matrix[M][m]==target:
                return True
            elif matrix[M][m]>target:
                r=m-1
            else:
                l=m+1
        return False


        