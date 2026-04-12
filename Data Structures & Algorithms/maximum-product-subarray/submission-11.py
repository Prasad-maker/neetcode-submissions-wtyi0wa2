class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # mn,mx,res = 1,1,max(nums)
        # for n in nums:
        #     tmp = mx*n
        #     mx=max(mn*n,mx*n)
        #     mn=min(tmp,mn*n)
        #     res = max(res,mx)
        # return res
        res = max(nums)
        mn,mx = 1,1
        for num in nums:
            tmp=mx*num
            mx=max(tmp,mn*num,num)
            mn=min(tmp,mn*num,num)
            res=max(mx,res)
        return res

        