class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        cur_min = float("inf")
        while(l<=r):
            m=l+(r-l)//2
            cur_min = min(cur_min,nums[m])
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m-1
    
        return cur_min
            
        