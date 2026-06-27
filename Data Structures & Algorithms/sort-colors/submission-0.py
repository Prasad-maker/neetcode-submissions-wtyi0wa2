class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = [0]*3
        for num in nums:
            arr[num]+=1
        res = []
        index = 0
        for i in range(3):
            for j in range(arr[i]):
                nums[index] = i
                index+=1
        
        