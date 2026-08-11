class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hset = set()
        r = 0 
        for num in nums:
            if num in hset:
                return True
            hset.add(num)
            if len(hset)>k:
                hset.remove(nums[r])
                r+=1
        return False
        