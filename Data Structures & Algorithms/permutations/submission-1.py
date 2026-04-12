class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for n in nums:
            new_per = []
            for p in perms:
                for i in range(len(p)+1):
                    p_cp = p.copy()
                    p_cp.insert(i,n)
                    new_per.append(p_cp)
                perms = new_per
        return perms


        