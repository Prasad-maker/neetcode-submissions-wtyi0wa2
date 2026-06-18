class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxindex = 0
        for index,num in enumerate(nums):
            if index>maxindex:
                return False
            maxindex = max(maxindex,index+num)
        return True

        