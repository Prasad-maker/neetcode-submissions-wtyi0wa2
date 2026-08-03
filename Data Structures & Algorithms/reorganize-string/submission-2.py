class Solution:
    def reorganizeString(self, s: str) -> str:
        count = [0]*26
        res = [""]*len(s)
        total = 0
        for c in s:
            count[ord(c)-ord('a')]+= 1
        heap = []
        for i in range(26):
            heap.append((-count[i],chr(ord('a')+i)))
        heapq.heapify(heap)
        cur = 0
        while total<len(s):

            count,char = heapq.heappop(heap)
            count = -count
            print(count,char)
            if count>(len(s)+1)//2:
                return ""
            for i in range(count):
                res[cur]=char
                cur+=2
                if cur>=len(s):
                    cur=1
            total+=count

        return "".join(res)
        
        
        