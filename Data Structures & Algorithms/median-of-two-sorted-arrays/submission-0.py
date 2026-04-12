class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B=nums1,nums2
        M=(len(A)+len(B))//2
        total=len(A)+len(B)
        if len(A)>len(B):
            A,B=B,A
        l=0
        r=len(A)-1
        while(True):
            i=(l+r)//2
            j=M-i-2
            aleft =A[i] if i>=0 else -float("inf")
            aright=A[i+1] if i<len(A)-1 else float("inf")
            bleft =B[j] if j>=0 else -float("inf")
            bright=B[j+1] if j<len(B)-1 else float("inf")
            if aleft<=bright and aright>=bleft:
                return min(aright,bright) if total%2==1 else (max(aleft, bleft) + min(aright, bright))/2
            elif aleft>bright:
                r=i-1
            else:
                l=+1
        



        