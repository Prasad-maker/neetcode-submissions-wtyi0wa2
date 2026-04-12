class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        curset=0
        for n in nums:
            if n-1 not in numset:
                n+=1
                curset = 1
                while n in numset:
                    curset+=1
                    n+=1
            longest = max(longest,curset)
        return longest

        
        