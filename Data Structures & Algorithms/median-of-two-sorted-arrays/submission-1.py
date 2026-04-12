class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = (len(nums1)+len(nums2))//2
        total = len(nums1)+len(nums2)
        if len(nums1)>len(nums2):
            nums1,nums2 = nums2,nums1
        l,r= 0,len(nums1)-1
        while True:
            i = (l+r)//2
            j = m-i-2
            Aleft = nums1[i] if i>=0 else float("-inf")
            Aright = nums1[i+1] if i<len(nums1)-1 else float("inf")
            Bleft = nums2[j] if j>=0 else float("-inf")
            Bright = nums2[j+1] if j<len(nums2)-1 else float("inf")
            if Aleft<=Bright and Aright>=Bleft:
                if total%2:
                    return min(Aright,Bright)
                else:
                    return (min(Aright,Bright)+max(Aleft,Bleft))/2
            elif Aleft>Bright:
                r=i-1
            else:
                l=i+1


            



        