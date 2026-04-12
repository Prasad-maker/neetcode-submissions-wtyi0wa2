class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        s_list = []
        visited = set()
        for s in strs:
            s_list.append(sorted(list(s)))
        for i in range(len(s_list)):
            r=[]
            if i not in visited:
                visited.add(i)
                r.append(strs[i])
                for j in range(i+1,len(s_list)):
                    if j not in visited:
                        if s_list[i]==s_list[j]:
                            r.append(strs[j])
                            visited.add(j)
            if r:
                res.append(r)
        return res

        