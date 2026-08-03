class Solution:
    def reorganizeString(self, s: str) -> str:
        count = [0]*26
        res = [""]*len(s)
        total = 0
        for c in s:
            count[ord(c)-ord('a')]+= 1
        heap = []
        if max(count)>((len(s)+1)//2):
            return ""
        maxindex = count.index(max(count))
        
        total = count[maxindex]
        cur = 0
        maxchar = chr(maxindex+ord('a'))
        for i in range(count[maxindex]):
            res[cur] = maxchar
            cur+=2
        count[maxindex]= 0 
        for i in range(26):
            heap.append((count[i],chr(ord('a')+i)))
        if cur>=len(s):
            cur=1
        while total<len(s):
            count,char = heap.pop()
            for i in range(count):
                res[cur]=char
                cur+=2
                if cur>=len(s):
                    cur=1
            total+=count

        return "".join(res)
        
        
        