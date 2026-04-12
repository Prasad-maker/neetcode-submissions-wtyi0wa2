class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast,slow=0,0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast==slow:
                break
        new = 0
        while True:
            new = nums[new]
            slow = nums[slow]
            if new == slow:
                break
        return new

        