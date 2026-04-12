class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        mn,mx = 1,1
        for num in nums:
            tmp=mx*num
            mx=max(tmp,mn*num)
            mn=min(tmp,mn*num)
            res=max(mx,res)
        return res

        