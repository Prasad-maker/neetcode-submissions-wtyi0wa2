class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s1=set()
        for i in nums:
            if i in s1:
                return True
            s1.add(i)
        return False
        
         